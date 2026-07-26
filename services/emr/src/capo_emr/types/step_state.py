"""Generated from Smithy shape ``com.amazonaws.emr#StepState``."""

from typing import Literal, TypeAlias, cast

StepState: TypeAlias = Literal[
    "PENDING",
    "CANCEL_PENDING",
    "RUNNING",
    "COMPLETED",
    "CANCELLED",
    "FAILED",
    "INTERRUPTED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StepState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> StepState:
    return cast(StepState, data)
