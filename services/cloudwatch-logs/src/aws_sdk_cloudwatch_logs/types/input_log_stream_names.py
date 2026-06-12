"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#InputLogStreamNames``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.log_stream_name

InputLogStreamNames: TypeAlias = list[
    "aws_sdk_cloudwatch_logs.types.log_stream_name.LogStreamName"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InputLogStreamNames) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> InputLogStreamNames:
    return list(data)
