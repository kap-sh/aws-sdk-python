"""Generated from Smithy shape ``com.amazonaws.networkmanager#ConnectionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_networkmanager.errors import DeserializationError

ConnectionStatus: TypeAlias = Literal[
    "UP",
    "DOWN",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "UP",
        "DOWN",
    )
)


def serialize_json(value: ConnectionStatus) -> str:
    return value


def deserialize_json(data: str) -> ConnectionStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ConnectionStatus value: {data!r}")
    return cast(ConnectionStatus, data)
