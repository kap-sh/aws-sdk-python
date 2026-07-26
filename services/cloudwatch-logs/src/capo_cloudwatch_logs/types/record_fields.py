"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#RecordFields``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.field_header

RecordFields: TypeAlias = list["capo_cloudwatch_logs.types.field_header.FieldHeader"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RecordFields) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> RecordFields:
    return list(data)
