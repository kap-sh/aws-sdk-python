"""Generated from Smithy shape ``com.amazonaws.iotwireless#WirelessDeviceFrameInfo``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot_wireless.errors import DeserializationError

"""<p> <code>FrameInfo</code> of your wireless device resources for the trace content. Use FrameInfo to debug the communication between your LoRaWAN end devices and the network server.</p>"""
WirelessDeviceFrameInfo: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
    )
)


def serialize_json(value: WirelessDeviceFrameInfo) -> str:
    return value


def deserialize_json(data: str) -> WirelessDeviceFrameInfo:
    if data not in _VALUES:
        raise DeserializationError(f"unknown WirelessDeviceFrameInfo value: {data!r}")
    return cast(WirelessDeviceFrameInfo, data)
