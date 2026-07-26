"""Generated from Smithy shape ``com.amazonaws.sagemaker#AutoMLJobStatus``."""

from typing import Literal, TypeAlias, cast

AutoMLJobStatus: TypeAlias = Literal[
    "Completed",
    "InProgress",
    "Failed",
    "Stopped",
    "Stopping",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AutoMLJobStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AutoMLJobStatus:
    return cast(AutoMLJobStatus, data)
