"""Generated from Smithy shape ``com.amazonaws.ecs#PlatformDeviceType``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ecs.errors import DeserializationError

PlatformDeviceType: TypeAlias = Literal[
    "GPU",
    "NEURON_DEVICE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "GPU",
        "NEURON_DEVICE",
    )
)


def serialize_aws_json_1_1(value: PlatformDeviceType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PlatformDeviceType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PlatformDeviceType value: {data!r}")
    return cast(PlatformDeviceType, data)
