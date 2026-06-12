"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#Columns``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.column

Columns: TypeAlias = list["aws_sdk_cloudwatch_logs.types.column.Column"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Columns) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> Columns:
    return list(data)
