"""Generated from Smithy shape ``com.amazonaws.sagemaker#ProcessingJobStatus``."""

from typing import Literal, TypeAlias, cast

ProcessingJobStatus: TypeAlias = Literal[
    "InProgress",
    "Completed",
    "Failed",
    "Stopping",
    "Stopped",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProcessingJobStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ProcessingJobStatus:
    return cast(ProcessingJobStatus, data)
