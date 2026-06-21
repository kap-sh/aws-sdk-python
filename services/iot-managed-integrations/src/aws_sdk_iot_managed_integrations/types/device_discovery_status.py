"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#DeviceDiscoveryStatus``."""

from typing import Literal, TypeAlias, cast

DeviceDiscoveryStatus: TypeAlias = Literal[
    "RUNNING",
    "SUCCEEDED",
    "FAILED",
    "TIMED_OUT",
]


# --- restJson1 ser/de ---
def serialize_json(value: DeviceDiscoveryStatus) -> str:
    return value


def deserialize_json(data: str) -> DeviceDiscoveryStatus:
    return cast(DeviceDiscoveryStatus, data)
