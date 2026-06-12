"""Generated from Smithy shape ``com.amazonaws.ssoadmin#GrantType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sso_admin.errors import DeserializationError

GrantType: TypeAlias = Literal[
    "authorization_code",
    "refresh_token",
    "urn:ietf:params:oauth:grant-type:jwt-bearer",
    "urn:ietf:params:oauth:grant-type:token-exchange",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "authorization_code",
        "refresh_token",
        "urn:ietf:params:oauth:grant-type:jwt-bearer",
        "urn:ietf:params:oauth:grant-type:token-exchange",
    )
)


def serialize_aws_json_1_1(value: GrantType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> GrantType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown GrantType value: {data!r}")
    return cast(GrantType, data)
