"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#TableFields``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.string

TableFields: TypeAlias = list["aws_sdk_cloudwatch_logs.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TableFields) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> TableFields:
    return list(data)
