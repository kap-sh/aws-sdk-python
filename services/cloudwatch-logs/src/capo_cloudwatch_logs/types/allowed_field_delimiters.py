"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#AllowedFieldDelimiters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.field_delimiter

AllowedFieldDelimiters: TypeAlias = list[
    "capo_cloudwatch_logs.types.field_delimiter.FieldDelimiter"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AllowedFieldDelimiters) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> AllowedFieldDelimiters:
    return list(data)
