"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#CreateLogStreamRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudwatch_logs.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.log_group_name
    import capo_cloudwatch_logs.types.log_stream_name


class CreateLogStreamRequest(TypedDict, closed=True):
    log_group_name: "capo_cloudwatch_logs.types.log_group_name.LogGroupName"
    """<p>The name of the log group.</p>"""
    log_stream_name: "capo_cloudwatch_logs.types.log_stream_name.LogStreamName"
    """<p>The name of the log stream.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateLogStreamRequest) -> dict:
    out: dict = {}
    out["logGroupName"] = value["log_group_name"]
    out["logStreamName"] = value["log_stream_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateLogStreamRequest:
    out: CreateLogStreamRequest = {}  # type: ignore[typeddict-item]
    if data.get("logGroupName") is not None:
        out["log_group_name"] = data["logGroupName"]
    else:
        raise DeserializationError("CreateLogStreamRequest.log_group_name required")
    if data.get("logStreamName") is not None:
        out["log_stream_name"] = data["logStreamName"]
    else:
        raise DeserializationError("CreateLogStreamRequest.log_stream_name required")
    return out
