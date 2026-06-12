"""Generated from Smithy shape ``com.amazonaws.transfer#ExecutionErrorType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_transfer.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
        "PERMISSION_DENIED",
        "CUSTOM_STEP_FAILED",
        "THROTTLED",
        "ALREADY_EXISTS",
        "NOT_FOUND",
        "BAD_REQUEST",
        "TIMEOUT",
        "INTERNAL_SERVER_ERROR",
    )
)


def serialize_aws_json_1_1(value: ExecutionErrorType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ExecutionErrorType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ExecutionErrorType value: {data!r}")
    return cast(ExecutionErrorType, data)
