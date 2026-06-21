"""Generated from Smithy shape ``com.amazonaws.emr#StepExecutionState``."""

from typing import Literal, TypeAlias, cast

StepExecutionState: TypeAlias = Literal[
    "PENDING",
    "RUNNING",
    "CONTINUE",
    "COMPLETED",
    "CANCELLED",
    "FAILED",
    "INTERRUPTED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StepExecutionState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> StepExecutionState:
    return cast(StepExecutionState, data)
