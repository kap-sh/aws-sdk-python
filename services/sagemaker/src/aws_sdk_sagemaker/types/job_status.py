"""Generated from Smithy shape ``com.amazonaws.sagemaker#JobStatus``."""

from typing import Literal, TypeAlias, cast

JobStatus: TypeAlias = Literal[
    "InProgress",
    "Completed",
    "Failed",
    "Stopping",
    "Stopped",
    "Deleting",
    "DeleteFailed",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: JobStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> JobStatus:
    return cast(JobStatus, data)
