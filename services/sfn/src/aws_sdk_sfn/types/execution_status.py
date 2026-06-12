"""Generated from Smithy shape ``com.amazonaws.sfn#ExecutionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sfn.errors import DeserializationError

ExecutionStatus: TypeAlias = Literal[
    "RUNNING",
    "SUCCEEDED",
    "FAILED",
    "TIMED_OUT",
    "ABORTED",
    "PENDING_REDRIVE",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "RUNNING",
        "SUCCEEDED",
        "FAILED",
        "TIMED_OUT",
        "ABORTED",
        "PENDING_REDRIVE",
    )
)


def serialize_aws_json_1_0(value: ExecutionStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ExecutionStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ExecutionStatus value: {data!r}")
    return cast(ExecutionStatus, data)
