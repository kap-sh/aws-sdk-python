"""Generated from Smithy shape ``com.amazonaws.transfer#ExecutionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_transfer.errors import DeserializationError

ExecutionStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "COMPLETED",
    "EXCEPTION",
    "HANDLING_EXCEPTION",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IN_PROGRESS",
        "COMPLETED",
        "EXCEPTION",
        "HANDLING_EXCEPTION",
    )
)


def serialize_aws_json_1_1(value: ExecutionStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ExecutionStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ExecutionStatus value: {data!r}")
    return cast(ExecutionStatus, data)
