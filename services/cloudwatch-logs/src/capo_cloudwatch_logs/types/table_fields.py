"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#TableFields``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.string

TableFields: TypeAlias = list["capo_cloudwatch_logs.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TableFields) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> TableFields:
    return [item for item in data if item is not None]
