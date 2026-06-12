"""Generated from Smithy shape ``com.amazonaws.devicefarm#DeviceAvailability``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_device_farm.errors import DeserializationError

DeviceAvailability: TypeAlias = Literal[
    "TEMPORARY_NOT_AVAILABLE",
    "BUSY",
    "AVAILABLE",
    "HIGHLY_AVAILABLE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "TEMPORARY_NOT_AVAILABLE",
        "BUSY",
        "AVAILABLE",
        "HIGHLY_AVAILABLE",
    )
)


def serialize_aws_json_1_1(value: DeviceAvailability) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DeviceAvailability:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DeviceAvailability value: {data!r}")
    return cast(DeviceAvailability, data)
