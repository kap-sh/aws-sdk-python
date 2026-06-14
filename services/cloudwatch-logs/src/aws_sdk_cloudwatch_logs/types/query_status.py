"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#QueryStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudwatch_logs.errors import DeserializationError

QueryStatus: TypeAlias = Literal[
    "Scheduled",
    "Running",
    "Complete",
    "Failed",
    "Cancelled",
    "Timeout",
    "Unknown",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Scheduled",
        "Running",
        "Complete",
        "Failed",
        "Cancelled",
        "Timeout",
        "Unknown",
    )
)


def serialize_aws_json_1_1(value: QueryStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> QueryStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown QueryStatus value: {data!r}")
    return cast(QueryStatus, data)
