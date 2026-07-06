"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#CloudWatchLoggingOption``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_kinesis_analytics_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics_v2.types.log_stream_arn


class CloudWatchLoggingOption(TypedDict, closed=True):
    log_stream_arn: "aws_sdk_kinesis_analytics_v2.types.log_stream_arn.LogStreamARN"
    """<p>The ARN of the CloudWatch log to receive application messages.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CloudWatchLoggingOption) -> dict:
    out: dict = {}
    out["LogStreamARN"] = value["log_stream_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CloudWatchLoggingOption:
    out: CloudWatchLoggingOption = {}  # type: ignore[typeddict-item]
    if "LogStreamARN" in data:
        out["log_stream_arn"] = data["LogStreamARN"]
    else:
        raise DeserializationError("CloudWatchLoggingOption.log_stream_arn required")
    return out
