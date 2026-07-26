"""Generated from Smithy shape ``com.amazonaws.sagemaker#TrainingJobStatus``."""

from typing import Literal, TypeAlias, cast

TrainingJobStatus: TypeAlias = Literal[
    "InProgress",
    "Completed",
    "Failed",
    "Stopping",
    "Stopped",
    "Deleting",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TrainingJobStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TrainingJobStatus:
    return cast(TrainingJobStatus, data)
