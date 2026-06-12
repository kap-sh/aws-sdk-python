"""Generated from Smithy shape ``com.amazonaws.healthlake#ErrorCategory``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_healthlake.errors import DeserializationError

ErrorCategory: TypeAlias = Literal[
    "RETRYABLE_ERROR",
    "NON_RETRYABLE_ERROR",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "RETRYABLE_ERROR",
        "NON_RETRYABLE_ERROR",
    )
)


def serialize_aws_json_1_0(value: ErrorCategory) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ErrorCategory:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ErrorCategory value: {data!r}")
    return cast(ErrorCategory, data)
