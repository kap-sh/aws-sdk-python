"""Generated from Smithy shape ``com.amazonaws.iotwireless#WirelessDeviceEvent``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot_wireless.errors import DeserializationError

"""<p>The event for a log message, if the log message is tied to a wireless device.</p>"""
WirelessDeviceEvent: TypeAlias = Literal[
    "Join",
    "Rejoin",
    "Uplink_Data",
    "Downlink_Data",
    "Registration",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Join",
        "Rejoin",
        "Uplink_Data",
        "Downlink_Data",
        "Registration",
    )
)


def serialize_json(value: WirelessDeviceEvent) -> str:
    return value


def deserialize_json(data: str) -> WirelessDeviceEvent:
    if data not in _VALUES:
        raise DeserializationError(f"unknown WirelessDeviceEvent value: {data!r}")
    return cast(WirelessDeviceEvent, data)
