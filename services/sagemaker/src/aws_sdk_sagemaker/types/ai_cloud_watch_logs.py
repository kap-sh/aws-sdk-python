"""Generated from Smithy shape ``com.amazonaws.sagemaker#AICloudWatchLogs``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.string


class AICloudWatchLogs(TypedDict, closed=True):
    log_group_arn: NotRequired["aws_sdk_sagemaker.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the CloudWatch log group.</p>"""
    log_stream_name: NotRequired["aws_sdk_sagemaker.types.string.String"]
    """<p>The name of the CloudWatch log stream.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AICloudWatchLogs) -> dict:
    out: dict = {}
    if "log_group_arn" in value:
        out["LogGroupArn"] = value["log_group_arn"]
    if "log_stream_name" in value:
        out["LogStreamName"] = value["log_stream_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AICloudWatchLogs:
    out: AICloudWatchLogs = {}  # type: ignore[typeddict-item]
    if "LogGroupArn" in data:
        out["log_group_arn"] = data["LogGroupArn"]
    if "LogStreamName" in data:
        out["log_stream_name"] = data["LogStreamName"]
    return out
