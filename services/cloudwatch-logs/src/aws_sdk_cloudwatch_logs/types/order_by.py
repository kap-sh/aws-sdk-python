"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#OrderBy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudwatch_logs.errors import DeserializationError

OrderBy: TypeAlias = Literal[
    "LogStreamName",
    "LastEventTime",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "LogStreamName",
        "LastEventTime",
    )
)


def serialize_aws_json_1_1(value: OrderBy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OrderBy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OrderBy value: {data!r}")
    return cast(OrderBy, data)
