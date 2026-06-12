"""Generated from Smithy shape ``com.amazonaws.appfabric#AuthType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_appfabric.errors import DeserializationError

AuthType: TypeAlias = Literal[
    "oauth2",
    "apiKey",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "oauth2",
        "apiKey",
    )
)


def serialize_json(value: AuthType) -> str:
    return value


def deserialize_json(data: str) -> AuthType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AuthType value: {data!r}")
    return cast(AuthType, data)
