"""Generated from Smithy shape ``com.amazonaws.iotwireless#WirelessDeviceFrameInfo``."""

from typing import Literal, TypeAlias, cast

"""<p> <code>FrameInfo</code> of your wireless device resources for the trace content. Use FrameInfo to debug the communication between your LoRaWAN end devices and the network server.</p>"""
WirelessDeviceFrameInfo: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: WirelessDeviceFrameInfo) -> str:
    return value


def deserialize_json(data: str) -> WirelessDeviceFrameInfo:
    return cast(WirelessDeviceFrameInfo, data)
