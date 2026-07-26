"""Generated from Smithy shape ``com.amazonaws.greengrassv2#CoreDeviceStatus``."""

from typing import Literal, TypeAlias, cast

CoreDeviceStatus: TypeAlias = Literal[
    "HEALTHY",
    "UNHEALTHY",
]


# --- restJson1 ser/de ---
def serialize_json(value: CoreDeviceStatus) -> str:
    return value


def deserialize_json(data: str) -> CoreDeviceStatus:
    return cast(CoreDeviceStatus, data)
