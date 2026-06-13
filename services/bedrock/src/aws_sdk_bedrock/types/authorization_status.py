"""Generated from Smithy shape ``com.amazonaws.bedrock#AuthorizationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock.errors import DeserializationError

AuthorizationStatus: TypeAlias = Literal[
    "AUTHORIZED",
    "NOT_AUTHORIZED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AUTHORIZED",
        "NOT_AUTHORIZED",
    )
)


def serialize_json(value: AuthorizationStatus) -> str:
    return value


def deserialize_json(data: str) -> AuthorizationStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AuthorizationStatus value: {data!r}")
    return cast(AuthorizationStatus, data)
