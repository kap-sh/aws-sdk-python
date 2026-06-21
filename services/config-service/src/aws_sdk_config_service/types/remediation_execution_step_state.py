"""Generated from Smithy shape ``com.amazonaws.configservice#RemediationExecutionStepState``."""

from typing import Literal, TypeAlias, cast

RemediationExecutionStepState: TypeAlias = Literal[
    "SUCCEEDED",
    "PENDING",
    "FAILED",
    "IN_PROGRESS",
    "EXITED",
    "UNKNOWN",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RemediationExecutionStepState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RemediationExecutionStepState:
    return cast(RemediationExecutionStepState, data)
