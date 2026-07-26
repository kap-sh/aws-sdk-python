"""Generated from Smithy shape ``com.amazonaws.sagemaker#TargetPlatformOs``."""

from typing import Literal, TypeAlias, cast

TargetPlatformOs: TypeAlias = Literal[
    "ANDROID",
    "LINUX",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TargetPlatformOs) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TargetPlatformOs:
    return cast(TargetPlatformOs, data)
