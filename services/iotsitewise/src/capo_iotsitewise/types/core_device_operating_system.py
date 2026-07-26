"""Generated from Smithy shape ``com.amazonaws.iotsitewise#CoreDeviceOperatingSystem``."""

from typing import Literal, TypeAlias, cast

CoreDeviceOperatingSystem: TypeAlias = Literal[
    "LINUX_AARCH64",
    "LINUX_AMD64",
    "WINDOWS_AMD64",
]


# --- restJson1 ser/de ---
def serialize_json(value: CoreDeviceOperatingSystem) -> str:
    return value


def deserialize_json(data: str) -> CoreDeviceOperatingSystem:
    return cast(CoreDeviceOperatingSystem, data)
