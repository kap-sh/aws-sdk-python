"""Generated from Smithy shape ``com.amazonaws.iotsitewise#CoreDeviceOperatingSystem``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iotsitewise.errors import DeserializationError

CoreDeviceOperatingSystem: TypeAlias = Literal[
    "LINUX_AARCH64",
    "LINUX_AMD64",
    "WINDOWS_AMD64",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "LINUX_AARCH64",
        "LINUX_AMD64",
        "WINDOWS_AMD64",
    )
)


def serialize_json(value: CoreDeviceOperatingSystem) -> str:
    return value


def deserialize_json(data: str) -> CoreDeviceOperatingSystem:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CoreDeviceOperatingSystem value: {data!r}")
    return cast(CoreDeviceOperatingSystem, data)
