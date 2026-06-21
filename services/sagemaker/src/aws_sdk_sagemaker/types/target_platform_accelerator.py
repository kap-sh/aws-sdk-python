"""Generated from Smithy shape ``com.amazonaws.sagemaker#TargetPlatformAccelerator``."""

from typing import Literal, TypeAlias, cast

TargetPlatformAccelerator: TypeAlias = Literal[
    "INTEL_GRAPHICS",
    "MALI",
    "NVIDIA",
    "NNA",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TargetPlatformAccelerator) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TargetPlatformAccelerator:
    return cast(TargetPlatformAccelerator, data)
