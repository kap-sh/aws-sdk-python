"""Generated from Smithy shape ``com.amazonaws.quicksight#ConnectionAuthType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

ConnectionAuthType: TypeAlias = Literal[
    "BASIC",
    "API_KEY",
    "OAUTH2_CLIENT_CREDENTIALS",
    "NONE",
    "IAM",
    "OAUTH2_AUTHORIZATION_CODE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "BASIC",
        "API_KEY",
        "OAUTH2_CLIENT_CREDENTIALS",
        "NONE",
        "IAM",
        "OAUTH2_AUTHORIZATION_CODE",
    )
)


def serialize_json(value: ConnectionAuthType) -> str:
    return value


def deserialize_json(data: str) -> ConnectionAuthType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ConnectionAuthType value: {data!r}")
    return cast(ConnectionAuthType, data)
