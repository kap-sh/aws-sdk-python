"""Generated from Smithy shape ``com.amazonaws.iotwireless#PositionResourceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot_wireless.errors import DeserializationError

PositionResourceType: TypeAlias = Literal[
    "WirelessDevice",
    "WirelessGateway",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "WirelessDevice",
        "WirelessGateway",
    )
)


def serialize_json(value: PositionResourceType) -> str:
    return value


def deserialize_json(data: str) -> PositionResourceType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PositionResourceType value: {data!r}")
    return cast(PositionResourceType, data)
