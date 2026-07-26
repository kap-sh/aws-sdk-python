"""Generated from Smithy shape ``com.amazonaws.ecs#PlatformDeviceType``."""

from typing import Literal, TypeAlias, cast

PlatformDeviceType: TypeAlias = Literal[
    "GPU",
    "NEURON_DEVICE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PlatformDeviceType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PlatformDeviceType:
    return cast(PlatformDeviceType, data)
