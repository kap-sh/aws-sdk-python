"""Generated from Smithy shape ``com.amazonaws.sfn#SyncExecutionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sfn.errors import DeserializationError

SyncExecutionStatus: TypeAlias = Literal[
    "SUCCEEDED",
    "FAILED",
    "TIMED_OUT",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SUCCEEDED",
        "FAILED",
        "TIMED_OUT",
    )
)


def serialize_aws_json_1_0(value: SyncExecutionStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> SyncExecutionStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SyncExecutionStatus value: {data!r}")
    return cast(SyncExecutionStatus, data)
