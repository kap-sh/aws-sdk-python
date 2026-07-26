"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#OrderBy``."""

from typing import Literal, TypeAlias, cast

OrderBy: TypeAlias = Literal[
    "LogStreamName",
    "LastEventTime",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OrderBy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OrderBy:
    return cast(OrderBy, data)
