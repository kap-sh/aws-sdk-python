"""Generated from Smithy shape ``com.amazonaws.mediaconnect#ConnectionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconnect.errors import DeserializationError

ConnectionStatus: TypeAlias = Literal[
    "CONNECTED",
    "DISCONNECTED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CONNECTED",
        "DISCONNECTED",
    )
)


def serialize_json(value: ConnectionStatus) -> str:
    return value


def deserialize_json(data: str) -> ConnectionStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ConnectionStatus value: {data!r}")
    return cast(ConnectionStatus, data)
