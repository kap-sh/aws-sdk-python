"""Generated from Smithy shape ``com.amazonaws.sagemaker#OptimizationJobStatus``."""

from typing import Literal, TypeAlias, cast

OptimizationJobStatus: TypeAlias = Literal[
    "INPROGRESS",
    "COMPLETED",
    "FAILED",
    "STARTING",
    "STOPPING",
    "STOPPED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OptimizationJobStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OptimizationJobStatus:
    return cast(OptimizationJobStatus, data)
