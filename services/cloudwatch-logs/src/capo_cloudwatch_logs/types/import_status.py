"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#ImportStatus``."""

from typing import Literal, TypeAlias, cast

ImportStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "CANCELLED",
    "COMPLETED",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImportStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ImportStatus:
    return cast(ImportStatus, data)
