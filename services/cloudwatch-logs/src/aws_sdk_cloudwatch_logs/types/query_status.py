"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#QueryStatus``."""

from typing import Literal, TypeAlias, cast

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
def serialize_aws_json_1_1(value: QueryStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> QueryStatus:
    return cast(QueryStatus, data)
