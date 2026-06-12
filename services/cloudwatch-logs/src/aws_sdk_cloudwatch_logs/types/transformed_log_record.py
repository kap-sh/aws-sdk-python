"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#TransformedLogRecord``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.event_message
    import aws_sdk_cloudwatch_logs.types.event_number
    import aws_sdk_cloudwatch_logs.types.transformed_event_message


class TransformedLogRecord(TypedDict):
    event_number: "aws_sdk_cloudwatch_logs.types.event_number.EventNumber"
    """<p>The event number.</p>"""
    event_message: NotRequired[
        "aws_sdk_cloudwatch_logs.types.event_message.EventMessage"
    ]
    """<p>The original log event message before it was transformed.</p>"""
    transformed_event_message: NotRequired[
        "aws_sdk_cloudwatch_logs.types.transformed_event_message.TransformedEventMessage"
    ]
    """<p>The log event message after being transformed.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TransformedLogRecord) -> dict:
    out: dict = {}
    out["eventNumber"] = value.get("event_number", 0)
    if "event_message" in value:
        out["eventMessage"] = value["event_message"]
    if "transformed_event_message" in value:
        out["transformedEventMessage"] = value["transformed_event_message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TransformedLogRecord:
    out: TransformedLogRecord = {}  # type: ignore[typeddict-item]
    if "eventNumber" in data:
        out["event_number"] = data["eventNumber"]
    else:
        out["event_number"] = 0
    if "eventMessage" in data:
        out["event_message"] = data["eventMessage"]
    if "transformedEventMessage" in data:
        out["transformed_event_message"] = data["transformedEventMessage"]
    return out
