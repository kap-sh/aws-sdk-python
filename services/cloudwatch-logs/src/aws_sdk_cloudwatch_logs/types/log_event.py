"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#LogEvent``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.event_message
    import aws_sdk_cloudwatch_logs.types.timestamp


class LogEvent(TypedDict):
    timestamp: NotRequired["aws_sdk_cloudwatch_logs.types.timestamp.Timestamp"]
    """<p>The time stamp of the log event.</p>"""
    message: NotRequired["aws_sdk_cloudwatch_logs.types.event_message.EventMessage"]
    """<p>The message content of the log event.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LogEvent) -> dict:
    out: dict = {}
    if "timestamp" in value:
        out["timestamp"] = value["timestamp"]
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> LogEvent:
    out: LogEvent = {}  # type: ignore[typeddict-item]
    if "timestamp" in data:
        out["timestamp"] = data["timestamp"]
    if "message" in data:
        out["message"] = data["message"]
    return out
