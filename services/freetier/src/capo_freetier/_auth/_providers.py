from __future__ import annotations

import configparser
import os
from abc import abstractmethod
from datetime import datetime, timezone
from pathlib import Path
from typing import Generic, TypeVar

from zapros import AsyncClient, Client, ZaprosError

from capo_freetier._auth._identity import (
    Credentials,
    Identity,
)
from capo_freetier._services._aws_config import _load_profile


class IdentityNotFound(Exception):
    """Raised when a provider cannot resolve an identity. Chain continues."""


IdentityT = TypeVar("IdentityT", bound="Identity")


class IdentityProvider(Generic[IdentityT]):
    @abstractmethod
    def resolve_identity(self) -> IdentityT:
        raise NotImplementedError

    async def aresolve_identity(self) -> IdentityT:
        # default: no network I/O, reuse the sync resolution
        return self.resolve_identity()


class ChainedProvider(IdentityProvider[IdentityT]):
    """Try each provider in order; first non-`IdentityNotFound` wins."""

    def __init__(self, *providers: IdentityProvider[IdentityT]) -> None:
        if not providers:
            raise ValueError("ChainedProvider requires at least one provider")
        self._providers = providers

    def resolve_identity(self) -> IdentityT:
        errors: list[str] = []
        for p in self._providers:
            try:
                return p.resolve_identity()
            except IdentityNotFound as e:
                errors.append(f"{type(p).__name__}: {e}")
        raise IdentityNotFound("no provider succeeded: " + "; ".join(errors))

    async def aresolve_identity(self) -> IdentityT:
        errors: list[str] = []
        for p in self._providers:
            try:
                return await p.aresolve_identity()
            except IdentityNotFound as e:
                errors.append(f"{type(p).__name__}: {e}")
        raise IdentityNotFound("no provider succeeded: " + "; ".join(errors))


class CachedProvider(IdentityProvider[IdentityT]):
    """Cache an identity until its `expiration` (minus skew) elapses."""

    _SKEW_SECONDS = 60

    def __init__(self, inner: IdentityProvider[IdentityT]) -> None:
        self._inner = inner
        self._cached: IdentityT | None = None

    def resolve_identity(self) -> IdentityT:
        if self._cached is not None and not self._expired(self._cached):
            return self._cached
        self._cached = self._inner.resolve_identity()
        return self._cached

    async def aresolve_identity(self) -> IdentityT:
        if self._cached is not None and not self._expired(self._cached):
            return self._cached
        self._cached = await self._inner.aresolve_identity()
        return self._cached

    @classmethod
    def _expired(cls, ident: Identity) -> bool:
        exp = ident.get("expiration")
        if exp is None:
            return False
        return (exp - datetime.now(timezone.utc)).total_seconds() <= cls._SKEW_SECONDS


class CredentialsProvider(IdentityProvider[Credentials]):
    """Base class for providers that resolve AWS `Credentials`."""

    @abstractmethod
    def resolve_identity(self) -> Credentials:
        raise NotImplementedError


class StaticAwsCredentialsProvider(CredentialsProvider):
    def __init__(self, credentials: Credentials) -> None:
        self._credentials = credentials

    def resolve_identity(self) -> Credentials:
        return self._credentials


class EnvCredentialsProvider(CredentialsProvider):
    """Read AWS_ACCESS_KEY_ID / AWS_SECRET_ACCESS_KEY / AWS_SESSION_TOKEN."""

    def resolve_identity(self) -> Credentials:
        ak = os.environ.get("AWS_ACCESS_KEY_ID")
        sk = os.environ.get("AWS_SECRET_ACCESS_KEY")
        if not ak or not sk:
            raise IdentityNotFound("AWS_ACCESS_KEY_ID / AWS_SECRET_ACCESS_KEY unset")
        out: Credentials = {"access_key": ak, "secret_key": sk}
        token = os.environ.get("AWS_SESSION_TOKEN")
        if token:
            out["session_token"] = token
        return out


class ProfileCredentialsProvider(CredentialsProvider):
    """Read ~/.aws/credentials and ~/.aws/config for the active profile."""

    def __init__(self, credentials_file: Path | None = None) -> None:
        self._profile = (
            os.environ.get("AWS_PROFILE")
            or os.environ.get("AWS_DEFAULT_PROFILE")
            or "default"
        )
        self._cred_file = credentials_file or Path(
            os.environ.get("AWS_SHARED_CREDENTIALS_FILE")
            or Path.home() / ".aws" / "credentials"
        )

    def resolve_identity(self) -> Credentials:
        section = self._load_section()
        ak = section.get("aws_access_key_id")
        sk = section.get("aws_secret_access_key")
        if not ak or not sk:
            raise IdentityNotFound(
                f"profile {self._profile!r}: missing aws_access_key_id/aws_secret_access_key"
            )
        out: Credentials = {"access_key": ak, "secret_key": sk}
        token = section.get("aws_session_token")
        if token:
            out["session_token"] = token
        return out

    def _load_section(self) -> dict[str, str]:
        # config-file profile reuses the loader from _services/_aws_config
        merged, _ = _load_profile()
        if self._cred_file.is_file():
            cfg = configparser.ConfigParser(interpolation=None)
            cfg.read(self._cred_file)
            if cfg.has_section(self._profile):
                merged.update(dict(cfg.items(self._profile)))
        if not merged:
            raise IdentityNotFound(
                f"profile {self._profile!r} not found in credentials/config files"
            )
        return merged


class EcsContainerCredentialsProvider(CredentialsProvider):
    """Resolve credentials from the ECS/EKS container credentials endpoint."""

    def __init__(self, client: Client | AsyncClient) -> None:
        self._client = client

    def resolve_identity(self) -> Credentials:
        if isinstance(self._client, AsyncClient):
            raise TypeError(
                "EcsContainerCredentialsProvider configured with AsyncClient; use aresolve_identity"
            )
        url, headers = self._request_args()
        resp = self._client.get(url, headers=headers)
        if resp.status < 200 or resp.status >= 300:
            raise IdentityNotFound(
                f"ECS credentials endpoint returned status {resp.status}"
            )
        return _credentials_from_json(resp.json)

    async def aresolve_identity(self) -> Credentials:
        if not isinstance(self._client, AsyncClient):
            raise TypeError(
                "EcsContainerCredentialsProvider configured with sync Client; use resolve_identity"
            )
        url, headers = self._request_args()
        resp = await self._client.get(url, headers=headers)
        if resp.status < 200 or resp.status >= 300:
            raise IdentityNotFound(
                f"ECS credentials endpoint returned status {resp.status}"
            )
        return _credentials_from_json(resp.json)

    def _request_args(self) -> tuple[str, dict[str, str]]:
        relative = os.environ.get("AWS_CONTAINER_CREDENTIALS_RELATIVE_URI")
        full = os.environ.get("AWS_CONTAINER_CREDENTIALS_FULL_URI")
        if relative:
            url = "http://169.254.170.2" + relative
        elif full:
            url = full
        else:
            raise IdentityNotFound("no ECS container credentials env var set")
        headers: dict[str, str] = {}
        token = os.environ.get("AWS_CONTAINER_AUTHORIZATION_TOKEN")
        token_file = os.environ.get("AWS_CONTAINER_AUTHORIZATION_TOKEN_FILE")
        if token_file:
            token = Path(token_file).read_text().strip()
        if token:
            headers["Authorization"] = token
        return url, headers


class Ec2InstanceMetadataProvider(CredentialsProvider):
    """Resolve credentials from the EC2 Instance Metadata Service (IMDSv2)."""

    _BASE = "http://169.254.169.254"
    _TOKEN_PATH = "/latest/api/token"
    _CREDS_PATH = "/latest/meta-data/iam/security-credentials/"

    def __init__(self, client: Client | AsyncClient) -> None:
        self._client = client

    def resolve_identity(self) -> Credentials:
        if isinstance(self._client, AsyncClient):
            raise TypeError(
                "Ec2InstanceMetadataProvider configured with AsyncClient; use aresolve_identity"
            )
        if os.environ.get("AWS_EC2_METADATA_DISABLED", "").strip().lower() in (
            "true",
            "1",
        ):
            raise IdentityNotFound("IMDS disabled via AWS_EC2_METADATA_DISABLED")
        try:
            token_resp = self._client.put(
                self._BASE + self._TOKEN_PATH,
                headers={"X-aws-ec2-metadata-token-ttl-seconds": "21600"},
                body=b"",
            )
            auth = {"X-aws-ec2-metadata-token": token_resp.text}
            role_resp = self._client.get(self._BASE + self._CREDS_PATH, headers=auth)
            role = role_resp.text.strip()
            creds_resp = self._client.get(
                self._BASE + self._CREDS_PATH + role, headers=auth
            )
        except ZaprosError as e:
            raise IdentityNotFound(f"IMDS request failed: {e}")
        if creds_resp.status < 200 or creds_resp.status >= 300:
            raise IdentityNotFound(f"IMDS returned status {creds_resp.status}")
        return _credentials_from_json(creds_resp.json)

    async def aresolve_identity(self) -> Credentials:
        if not isinstance(self._client, AsyncClient):
            raise TypeError(
                "Ec2InstanceMetadataProvider configured with sync Client; use resolve_identity"
            )
        if os.environ.get("AWS_EC2_METADATA_DISABLED", "").strip().lower() in (
            "true",
            "1",
        ):
            raise IdentityNotFound("IMDS disabled via AWS_EC2_METADATA_DISABLED")
        try:
            token_resp = await self._client.put(
                self._BASE + self._TOKEN_PATH,
                headers={"X-aws-ec2-metadata-token-ttl-seconds": "21600"},
                body=b"",
            )
            auth = {"X-aws-ec2-metadata-token": token_resp.text}
            role_resp = await self._client.get(
                self._BASE + self._CREDS_PATH, headers=auth
            )
            role = role_resp.text.strip()
            creds_resp = await self._client.get(
                self._BASE + self._CREDS_PATH + role, headers=auth
            )
        except ZaprosError as e:
            raise IdentityNotFound(f"IMDS request failed: {e}")
        if creds_resp.status < 200 or creds_resp.status >= 300:
            raise IdentityNotFound(f"IMDS returned status {creds_resp.status}")
        return _credentials_from_json(creds_resp.json)


def _parse_iso8601(value: str) -> datetime:
    # tolerate trailing 'Z'
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def _credentials_from_json(data: dict[str, object]) -> Credentials:
    ak = data.get("AccessKeyId")
    sk = data.get("SecretAccessKey")
    if not isinstance(ak, str) or not isinstance(sk, str):
        raise IdentityNotFound(
            "credentials response missing AccessKeyId/SecretAccessKey"
        )
    out: Credentials = {"access_key": ak, "secret_key": sk}
    token = data.get("Token")
    if isinstance(token, str):
        out["session_token"] = token
    exp = data.get("Expiration")
    if isinstance(exp, str):
        out["expiration"] = _parse_iso8601(exp)
    return out


def default_aws_credentials_chain(
    client: Client | AsyncClient,
) -> IdentityProvider[Credentials]:
    return CachedProvider(
        ChainedProvider(
            EnvCredentialsProvider(),
            ProfileCredentialsProvider(),
            EcsContainerCredentialsProvider(client),
            Ec2InstanceMetadataProvider(client),
        )
    )
