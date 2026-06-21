"""Generated from Smithy shape ``com.amazonaws.iotwireless#DeviceState``."""

from typing import Literal, TypeAlias, cast

"""<p>Device state defines the device status of sidewalk device.</p>"""
DeviceState: TypeAlias = Literal[
    "Provisioned",
    "RegisteredNotSeen",
    "RegisteredReachable",
    "RegisteredUnreachable",
]


# --- restJson1 ser/de ---
def serialize_json(value: DeviceState) -> str:
    return value


def deserialize_json(data: str) -> DeviceState:
    return cast(DeviceState, data)
