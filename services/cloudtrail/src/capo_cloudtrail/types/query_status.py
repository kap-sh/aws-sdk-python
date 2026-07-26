"""Generated from Smithy shape ``com.amazonaws.cloudtrail#QueryStatus``."""

from typing import Literal, TypeAlias, cast

QueryStatus: TypeAlias = Literal[
    "QUEUED",
    "RUNNING",
    "FINISHED",
    "FAILED",
    "CANCELLED",
    "TIMED_OUT",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: QueryStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> QueryStatus:
    return cast(QueryStatus, data)
