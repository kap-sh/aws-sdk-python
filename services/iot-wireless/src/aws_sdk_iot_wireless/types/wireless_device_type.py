"""Generated from Smithy shape ``com.amazonaws.iotwireless#WirelessDeviceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot_wireless.errors import DeserializationError

WirelessDeviceType: TypeAlias = Literal[
    "Sidewalk",
    "LoRaWAN",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Sidewalk",
        "LoRaWAN",
    )
)


def serialize_json(value: WirelessDeviceType) -> str:
    return value


def deserialize_json(data: str) -> WirelessDeviceType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown WirelessDeviceType value: {data!r}")
    return cast(WirelessDeviceType, data)
