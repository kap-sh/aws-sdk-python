"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#DeleteLogStreamRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cloudwatch_logs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.log_group_name
    import aws_sdk_cloudwatch_logs.types.log_stream_name


class DeleteLogStreamRequest(TypedDict, closed=True):
    log_group_name: "aws_sdk_cloudwatch_logs.types.log_group_name.LogGroupName"
    """<p>The name of the log group.</p>"""
    log_stream_name: "aws_sdk_cloudwatch_logs.types.log_stream_name.LogStreamName"
    """<p>The name of the log stream.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteLogStreamRequest) -> dict:
    out: dict = {}
    out["logGroupName"] = value["log_group_name"]
    out["logStreamName"] = value["log_stream_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteLogStreamRequest:
    out: DeleteLogStreamRequest = {}  # type: ignore[typeddict-item]
    if "logGroupName" in data:
        out["log_group_name"] = data["logGroupName"]
    else:
        raise DeserializationError("DeleteLogStreamRequest.log_group_name required")
    if "logStreamName" in data:
        out["log_stream_name"] = data["logStreamName"]
    else:
        raise DeserializationError("DeleteLogStreamRequest.log_stream_name required")
    return out
