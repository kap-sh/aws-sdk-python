"""Generated from Smithy shape ``com.amazonaws.configservice#RemediationExecutionState``."""

from typing import Literal, TypeAlias, cast

RemediationExecutionState: TypeAlias = Literal[
    "QUEUED",
    "IN_PROGRESS",
    "SUCCEEDED",
    "FAILED",
    "UNKNOWN",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RemediationExecutionState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RemediationExecutionState:
    return cast(RemediationExecutionState, data)
