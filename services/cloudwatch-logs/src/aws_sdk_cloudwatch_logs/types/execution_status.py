"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#ExecutionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudwatch_logs.errors import DeserializationError

ExecutionStatus: TypeAlias = Literal[
    "Running",
    "InvalidQuery",
    "Complete",
    "Failed",
    "Timeout",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Running",
        "InvalidQuery",
        "Complete",
        "Failed",
        "Timeout",
    )
)


def serialize_aws_json_1_1(value: ExecutionStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ExecutionStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ExecutionStatus value: {data!r}")
    return cast(ExecutionStatus, data)
