"""Generated from Smithy shape ``com.amazonaws.healthlake#ErrorCategory``."""

from typing import Literal, TypeAlias, cast

ErrorCategory: TypeAlias = Literal[
    "RETRYABLE_ERROR",
    "NON_RETRYABLE_ERROR",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ErrorCategory) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ErrorCategory:
    return cast(ErrorCategory, data)
