"""Generated from Smithy shape ``com.amazonaws.iotwireless#ConnectionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot_wireless.errors import DeserializationError

ConnectionStatus: TypeAlias = Literal[
    "Connected",
    "Disconnected",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Connected",
        "Disconnected",
    )
)


def serialize_json(value: ConnectionStatus) -> str:
    return value


def deserialize_json(data: str) -> ConnectionStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ConnectionStatus value: {data!r}")
    return cast(ConnectionStatus, data)
