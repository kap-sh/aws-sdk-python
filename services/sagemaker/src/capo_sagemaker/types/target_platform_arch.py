"""Generated from Smithy shape ``com.amazonaws.sagemaker#TargetPlatformArch``."""

from typing import Literal, TypeAlias, cast

TargetPlatformArch: TypeAlias = Literal[
    "X86_64",
    "X86",
    "ARM64",
    "ARM_EABI",
    "ARM_EABIHF",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TargetPlatformArch) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TargetPlatformArch:
    return cast(TargetPlatformArch, data)
