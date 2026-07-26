"""Generated from Smithy shape ``com.amazonaws.iotwireless#DeviceProfileType``."""

from typing import Literal, TypeAlias, cast

DeviceProfileType: TypeAlias = Literal[
    "Sidewalk",
    "LoRaWAN",
]


# --- restJson1 ser/de ---
def serialize_json(value: DeviceProfileType) -> str:
    return value


def deserialize_json(data: str) -> DeviceProfileType:
    return cast(DeviceProfileType, data)
