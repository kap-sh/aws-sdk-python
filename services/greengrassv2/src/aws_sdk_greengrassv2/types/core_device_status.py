"""Generated from Smithy shape ``com.amazonaws.greengrassv2#CoreDeviceStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_greengrassv2.errors import DeserializationError

CoreDeviceStatus: TypeAlias = Literal[
    "HEALTHY",
    "UNHEALTHY",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "HEALTHY",
        "UNHEALTHY",
    )
)


def serialize_json(value: CoreDeviceStatus) -> str:
    return value


def deserialize_json(data: str) -> CoreDeviceStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CoreDeviceStatus value: {data!r}")
    return cast(CoreDeviceStatus, data)
