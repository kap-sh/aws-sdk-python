"""Generated from Smithy shape ``com.amazonaws.ssoadmin#TrustedTokenIssuerType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sso_admin.errors import DeserializationError

TrustedTokenIssuerType: TypeAlias = Literal["OIDC_JWT",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("OIDC_JWT",))


def serialize_aws_json_1_1(value: TrustedTokenIssuerType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TrustedTokenIssuerType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TrustedTokenIssuerType value: {data!r}")
    return cast(TrustedTokenIssuerType, data)
