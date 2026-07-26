"""Generated from Smithy shape ``com.amazonaws.iotwireless#WirelessDeviceSidewalkStatus``."""

from typing import Literal, TypeAlias, cast

WirelessDeviceSidewalkStatus: TypeAlias = Literal[
    "PROVISIONED",
    "REGISTERED",
    "ACTIVATED",
    "UNKNOWN",
]


# --- restJson1 ser/de ---
def serialize_json(value: WirelessDeviceSidewalkStatus) -> str:
    return value


def deserialize_json(data: str) -> WirelessDeviceSidewalkStatus:
    return cast(WirelessDeviceSidewalkStatus, data)
