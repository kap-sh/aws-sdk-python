"""Generated from Smithy shape ``com.amazonaws.kinesisanalytics#CloudWatchLoggingOptionUpdate``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_kinesis_analytics.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics.types.id
    import aws_sdk_kinesis_analytics.types.log_stream_arn
    import aws_sdk_kinesis_analytics.types.role_arn


class CloudWatchLoggingOptionUpdate(TypedDict):
    cloud_watch_logging_option_id: "aws_sdk_kinesis_analytics.types.id.Id"
    """<p>ID of the CloudWatch logging option to update</p>"""
    log_stream_arn_update: NotRequired[
        "aws_sdk_kinesis_analytics.types.log_stream_arn.LogStreamARN"
    ]
    """<p>ARN of the CloudWatch log to receive application messages.</p>"""
    role_arn_update: NotRequired["aws_sdk_kinesis_analytics.types.role_arn.RoleARN"]
    """<p>IAM ARN of the role to use to send application messages. Note: To write application messages to CloudWatch, the IAM role used must have the <code>PutLogEvents</code> policy action enabled.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CloudWatchLoggingOptionUpdate) -> dict:
    out: dict = {}
    out["CloudWatchLoggingOptionId"] = value["cloud_watch_logging_option_id"]
    if "log_stream_arn_update" in value:
        out["LogStreamARNUpdate"] = value["log_stream_arn_update"]
    if "role_arn_update" in value:
        out["RoleARNUpdate"] = value["role_arn_update"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CloudWatchLoggingOptionUpdate:
    out: CloudWatchLoggingOptionUpdate = {}  # type: ignore[typeddict-item]
    if "CloudWatchLoggingOptionId" in data:
        out["cloud_watch_logging_option_id"] = data["CloudWatchLoggingOptionId"]
    else:
        raise DeserializationError(
            "CloudWatchLoggingOptionUpdate.cloud_watch_logging_option_id required"
        )
    if "LogStreamARNUpdate" in data:
        out["log_stream_arn_update"] = data["LogStreamARNUpdate"]
    if "RoleARNUpdate" in data:
        out["role_arn_update"] = data["RoleARNUpdate"]
    return out
