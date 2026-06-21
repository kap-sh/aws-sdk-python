"""Generated from Smithy shape ``com.amazonaws.sagemaker#TransformJobStatus``."""

from typing import Literal, TypeAlias, cast

TransformJobStatus: TypeAlias = Literal[
    "InProgress",
    "Completed",
    "Failed",
    "Stopping",
    "Stopped",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TransformJobStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TransformJobStatus:
    return cast(TransformJobStatus, data)
