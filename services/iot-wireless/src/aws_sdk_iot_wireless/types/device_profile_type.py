"""Generated from Smithy shape ``com.amazonaws.iotwireless#DeviceProfileType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot_wireless.errors import DeserializationError

DeviceProfileType: TypeAlias = Literal[
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


def serialize_json(value: DeviceProfileType) -> str:
    return value


def deserialize_json(data: str) -> DeviceProfileType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DeviceProfileType value: {data!r}")
    return cast(DeviceProfileType, data)
