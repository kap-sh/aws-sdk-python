"""Generated from Smithy shape ``com.amazonaws.iotwireless#WirelessDeviceIdType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot_wireless.errors import DeserializationError

WirelessDeviceIdType: TypeAlias = Literal[
    "WirelessDeviceId",
    "DevEui",
    "ThingName",
    "SidewalkManufacturingSn",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "WirelessDeviceId",
        "DevEui",
        "ThingName",
        "SidewalkManufacturingSn",
    )
)


def serialize_json(value: WirelessDeviceIdType) -> str:
    return value


def deserialize_json(data: str) -> WirelessDeviceIdType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown WirelessDeviceIdType value: {data!r}")
    return cast(WirelessDeviceIdType, data)
