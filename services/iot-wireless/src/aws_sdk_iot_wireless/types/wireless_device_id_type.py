"""Generated from Smithy shape ``com.amazonaws.iotwireless#WirelessDeviceIdType``."""

from typing import Literal, TypeAlias, cast

WirelessDeviceIdType: TypeAlias = Literal[
    "WirelessDeviceId",
    "DevEui",
    "ThingName",
    "SidewalkManufacturingSn",
]


# --- restJson1 ser/de ---
def serialize_json(value: WirelessDeviceIdType) -> str:
    return value


def deserialize_json(data: str) -> WirelessDeviceIdType:
    return cast(WirelessDeviceIdType, data)
