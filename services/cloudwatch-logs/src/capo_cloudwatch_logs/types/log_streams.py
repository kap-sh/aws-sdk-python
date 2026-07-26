"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#LogStreams``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.log_stream

LogStreams: TypeAlias = list["capo_cloudwatch_logs.types.log_stream.LogStream"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LogStreams) -> list:
    import capo_cloudwatch_logs.types.log_stream

    out: list = []
    for item in value:
        out.append(capo_cloudwatch_logs.types.log_stream.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> LogStreams:
    import capo_cloudwatch_logs.types.log_stream

    out: LogStreams = []
    for item in data:
        out.append(capo_cloudwatch_logs.types.log_stream.deserialize_aws_json_1_1(item))
    return out
