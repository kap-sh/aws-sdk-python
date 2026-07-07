"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#InputLogEvent``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cloudwatch_logs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.event_message
    import aws_sdk_cloudwatch_logs.types.timestamp


class InputLogEvent(TypedDict, closed=True):
    timestamp: "aws_sdk_cloudwatch_logs.types.timestamp.Timestamp"
    """<p>The time the event occurred, expressed as the number of milliseconds after <code>Jan 1, 1970 00:00:00 UTC</code>.</p>"""
    message: "aws_sdk_cloudwatch_logs.types.event_message.EventMessage"
    """<p>The raw event message. Each log event can be no larger than 1 MB.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InputLogEvent) -> dict:
    out: dict = {}
    out["timestamp"] = value["timestamp"]
    out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InputLogEvent:
    out: InputLogEvent = {}  # type: ignore[typeddict-item]
    if "timestamp" in data:
        out["timestamp"] = data["timestamp"]
    else:
        raise DeserializationError("InputLogEvent.timestamp required")
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("InputLogEvent.message required")
    return out
