"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#DeviceDiscoveryStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot_managed_integrations.errors import DeserializationError

DeviceDiscoveryStatus: TypeAlias = Literal[
    "RUNNING",
    "SUCCEEDED",
    "FAILED",
    "TIMED_OUT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "RUNNING",
        "SUCCEEDED",
        "FAILED",
        "TIMED_OUT",
    )
)


def serialize_json(value: DeviceDiscoveryStatus) -> str:
    return value


def deserialize_json(data: str) -> DeviceDiscoveryStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DeviceDiscoveryStatus value: {data!r}")
    return cast(DeviceDiscoveryStatus, data)
