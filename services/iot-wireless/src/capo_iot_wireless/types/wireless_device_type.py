"""Generated from Smithy shape ``com.amazonaws.iotwireless#WirelessDeviceType``."""

from typing import Literal, TypeAlias, cast

WirelessDeviceType: TypeAlias = Literal[
    "Sidewalk",
    "LoRaWAN",
]


# --- restJson1 ser/de ---
def serialize_json(value: WirelessDeviceType) -> str:
    return value


def deserialize_json(data: str) -> WirelessDeviceType:
    return cast(WirelessDeviceType, data)
