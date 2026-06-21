"""Generated from Smithy shape ``com.amazonaws.sagemaker#AutoMLChannelType``."""

from typing import Literal, TypeAlias, cast

AutoMLChannelType: TypeAlias = Literal[
    "training",
    "validation",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AutoMLChannelType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AutoMLChannelType:
    return cast(AutoMLChannelType, data)
