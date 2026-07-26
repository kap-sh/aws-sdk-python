"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#LogTypes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.log_type

LogTypes: TypeAlias = list["capo_cloudwatch_logs.types.log_type.LogType"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LogTypes) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> LogTypes:
    return list(data)
