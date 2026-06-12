"""Generated from Smithy shape ``com.amazonaws.devicefarm#DevicePoolType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_device_farm.errors import DeserializationError

DevicePoolType: TypeAlias = Literal[
    "CURATED",
    "PRIVATE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CURATED",
        "PRIVATE",
    )
)


def serialize_aws_json_1_1(value: DevicePoolType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DevicePoolType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DevicePoolType value: {data!r}")
    return cast(DevicePoolType, data)
