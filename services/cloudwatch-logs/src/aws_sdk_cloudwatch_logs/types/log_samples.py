"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#LogSamples``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.log_event

LogSamples: TypeAlias = list["aws_sdk_cloudwatch_logs.types.log_event.LogEvent"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LogSamples) -> list:
    import aws_sdk_cloudwatch_logs.types.log_event

    out: list = []
    for item in value:
        out.append(aws_sdk_cloudwatch_logs.types.log_event.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> LogSamples:
    import aws_sdk_cloudwatch_logs.types.log_event

    out: LogSamples = []
    for item in data:
        out.append(
            aws_sdk_cloudwatch_logs.types.log_event.deserialize_aws_json_1_1(item)
        )
    return out
