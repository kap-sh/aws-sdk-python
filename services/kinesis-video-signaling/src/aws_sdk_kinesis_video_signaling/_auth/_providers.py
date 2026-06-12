from __future__ import annotations

import configparser
import os
from abc import abstractmethod
from datetime import datetime, timezone
from pathlib import Path
from typing import Generic, TypeVar

from aws_sdk_kinesis_video_signaling._auth._identity import (
    Credentials,
    Identity,
)


class IdentityNotFound(Exception):
    """Raised when a provider cannot resolve an identity. Chain continues."""


IdentityT = TypeVar("IdentityT", bound="Identity")


class IdentityProvider(Generic[IdentityT]):
    @abstractmethod
    def resolve_identity(self) -> IdentityT:
        raise NotImplementedError


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

    def __init__(
        self,
        profile: str | None = None,
        credentials_file: Path | None = None,
        config_file: Path | None = None,
    ) -> None:
        self._profile = profile or os.environ.get("AWS_PROFILE", "default")
        self._cred_file = credentials_file or Path(
            os.environ.get("AWS_SHARED_CREDENTIALS_FILE")
            or Path.home() / ".aws" / "credentials"
        )
        self._cfg_file = config_file or Path(
            os.environ.get("AWS_CONFIG_FILE") or Path.home() / ".aws" / "config"
        )

    def resolve_identity(self) -> Credentials:
        section = self._load_profile()
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

    def _load_profile(self) -> dict[str, str]:
        merged: dict[str, str] = {}
        if self._cfg_file.is_file():
            cfg = configparser.ConfigParser()
            cfg.read(self._cfg_file)
            # config file profiles look like `[profile foo]`, except default
            key = (
                "default" if self._profile == "default" else f"profile {self._profile}"
            )
            if cfg.has_section(key):
                merged.update(dict(cfg.items(key)))
        if self._cred_file.is_file():
            cfg = configparser.ConfigParser()
            cfg.read(self._cred_file)
            if cfg.has_section(self._profile):
                merged.update(dict(cfg.items(self._profile)))
        if not merged:
            raise IdentityNotFound(
                f"profile {self._profile!r} not found in {self._cred_file} or {self._cfg_file}"
            )
        return merged


def default_aws_credentials_chain() -> IdentityProvider[Credentials]:
    return CachedProvider(
        ChainedProvider(EnvCredentialsProvider(), ProfileCredentialsProvider())
    )
