"""Generated from Smithy shape ``com.amazonaws.sagemaker#EdgePackagingJobStatus``."""

from typing import Literal, TypeAlias, cast

EdgePackagingJobStatus: TypeAlias = Literal[
    "STARTING",
    "INPROGRESS",
    "COMPLETED",
    "FAILED",
    "STOPPING",
    "STOPPED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EdgePackagingJobStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> EdgePackagingJobStatus:
    return cast(EdgePackagingJobStatus, data)
