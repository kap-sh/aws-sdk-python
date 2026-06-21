"""Generated from Smithy shape ``com.amazonaws.devicefarm#ExecutionResult``."""

from typing import Literal, TypeAlias, cast

ExecutionResult: TypeAlias = Literal[
    "PENDING",
    "PASSED",
    "WARNED",
    "FAILED",
    "SKIPPED",
    "ERRORED",
    "STOPPED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExecutionResult) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ExecutionResult:
    return cast(ExecutionResult, data)
