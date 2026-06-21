"""Generated from Smithy shape ``com.amazonaws.transfer#ExecutionErrorType``."""

from typing import Literal, TypeAlias, cast

ExecutionErrorType: TypeAlias = Literal[
    "PERMISSION_DENIED",
    "CUSTOM_STEP_FAILED",
    "THROTTLED",
    "ALREADY_EXISTS",
    "NOT_FOUND",
    "BAD_REQUEST",
    "TIMEOUT",
    "INTERNAL_SERVER_ERROR",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExecutionErrorType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ExecutionErrorType:
    return cast(ExecutionErrorType, data)
