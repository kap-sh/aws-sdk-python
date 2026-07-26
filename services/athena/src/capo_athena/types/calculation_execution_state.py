"""Generated from Smithy shape ``com.amazonaws.athena#CalculationExecutionState``."""

from typing import Literal, TypeAlias, cast

CalculationExecutionState: TypeAlias = Literal[
    "CREATING",
    "CREATED",
    "QUEUED",
    "RUNNING",
    "CANCELING",
    "CANCELED",
    "COMPLETED",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CalculationExecutionState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CalculationExecutionState:
    return cast(CalculationExecutionState, data)
