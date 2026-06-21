"""Generated from Smithy shape ``com.amazonaws.codepipeline#StageExecutionStatus``."""

from typing import Literal, TypeAlias, cast

StageExecutionStatus: TypeAlias = Literal[
    "Cancelled",
    "InProgress",
    "Failed",
    "Stopped",
    "Stopping",
    "Succeeded",
    "Skipped",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StageExecutionStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> StageExecutionStatus:
    return cast(StageExecutionStatus, data)
