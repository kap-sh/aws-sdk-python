"""Generated from Smithy shape ``com.amazonaws.glue#OAuth2GrantType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_glue.errors import DeserializationError

OAuth2GrantType: TypeAlias = Literal[
    "AUTHORIZATION_CODE",
    "CLIENT_CREDENTIALS",
    "JWT_BEARER",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AUTHORIZATION_CODE",
        "CLIENT_CREDENTIALS",
        "JWT_BEARER",
    )
)


def serialize_aws_json_1_1(value: OAuth2GrantType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OAuth2GrantType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OAuth2GrantType value: {data!r}")
    return cast(OAuth2GrantType, data)
