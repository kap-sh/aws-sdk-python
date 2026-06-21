"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#ExportTaskStatusCode``."""

from typing import Literal, TypeAlias, cast

ExportTaskStatusCode: TypeAlias = Literal[
    "CANCELLED",
    "COMPLETED",
    "FAILED",
    "PENDING",
    "PENDING_CANCEL",
    "RUNNING",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExportTaskStatusCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ExportTaskStatusCode:
    return cast(ExportTaskStatusCode, data)
