"""Generated from Smithy shape ``com.amazonaws.iotwireless#WirelessDeviceEvent``."""

from typing import Literal, TypeAlias, cast

"""<p>The event for a log message, if the log message is tied to a wireless device.</p>"""
WirelessDeviceEvent: TypeAlias = Literal[
    "Join",
    "Rejoin",
    "Uplink_Data",
    "Downlink_Data",
    "Registration",
]


# --- restJson1 ser/de ---
def serialize_json(value: WirelessDeviceEvent) -> str:
    return value


def deserialize_json(data: str) -> WirelessDeviceEvent:
    return cast(WirelessDeviceEvent, data)
