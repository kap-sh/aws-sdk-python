"""Generated from Smithy shape ``com.amazonaws.kinesisanalytics#CloudWatchLoggingOption``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_kinesis_analytics.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics.types.log_stream_arn
    import aws_sdk_kinesis_analytics.types.role_arn


class CloudWatchLoggingOption(TypedDict, closed=True):
    log_stream_arn: "aws_sdk_kinesis_analytics.types.log_stream_arn.LogStreamARN"
    """<p>ARN of the CloudWatch log to receive application messages.</p>"""
    role_arn: "aws_sdk_kinesis_analytics.types.role_arn.RoleARN"
    """<p>IAM ARN of the role to use to send application messages. Note: To write application messages to CloudWatch, the IAM role that is used must have the <code>PutLogEvents</code> policy action enabled.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CloudWatchLoggingOption) -> dict:
    out: dict = {}
    out["LogStreamARN"] = value["log_stream_arn"]
    out["RoleARN"] = value["role_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CloudWatchLoggingOption:
    out: CloudWatchLoggingOption = {}  # type: ignore[typeddict-item]
    if "LogStreamARN" in data:
        out["log_stream_arn"] = data["LogStreamARN"]
    else:
        raise DeserializationError("CloudWatchLoggingOption.log_stream_arn required")
    if "RoleARN" in data:
        out["role_arn"] = data["RoleARN"]
    else:
        raise DeserializationError("CloudWatchLoggingOption.role_arn required")
    return out
