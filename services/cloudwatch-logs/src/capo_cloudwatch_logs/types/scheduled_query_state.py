"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#ScheduledQueryState``."""

from typing import Literal, TypeAlias, cast

ScheduledQueryState: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ScheduledQueryState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ScheduledQueryState:
    return cast(ScheduledQueryState, data)
