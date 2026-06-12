"""Generated from Smithy shape ``com.amazonaws.glue#ConnectorOAuth2GrantType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_glue.errors import DeserializationError

ConnectorOAuth2GrantType: TypeAlias = Literal[
    "CLIENT_CREDENTIALS",
    "JWT_BEARER",
    "AUTHORIZATION_CODE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CLIENT_CREDENTIALS",
        "JWT_BEARER",
        "AUTHORIZATION_CODE",
    )
)


def serialize_aws_json_1_1(value: ConnectorOAuth2GrantType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ConnectorOAuth2GrantType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ConnectorOAuth2GrantType value: {data!r}")
    return cast(ConnectorOAuth2GrantType, data)
