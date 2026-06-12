"""Generated from Smithy shape ``com.amazonaws.iotwireless#PositioningConfigStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot_wireless.errors import DeserializationError

PositioningConfigStatus: TypeAlias = Literal[
    "Enabled",
    "Disabled",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Enabled",
        "Disabled",
    )
)


def serialize_json(value: PositioningConfigStatus) -> str:
    return value


def deserialize_json(data: str) -> PositioningConfigStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PositioningConfigStatus value: {data!r}")
    return cast(PositioningConfigStatus, data)
