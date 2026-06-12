"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#LogRecord``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.field
    import aws_sdk_cloudwatch_logs.types.value

LogRecord: TypeAlias = dict[
    "aws_sdk_cloudwatch_logs.types.field.Field",
    "aws_sdk_cloudwatch_logs.types.value.Value",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: LogRecord) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> LogRecord:
    out: LogRecord = {}
    for key, value in data.items():
        out[key] = value
    return out
