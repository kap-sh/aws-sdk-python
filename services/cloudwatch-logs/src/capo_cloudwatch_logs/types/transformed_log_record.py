"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#TransformedLogRecord``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.event_message
    import capo_cloudwatch_logs.types.event_number
    import capo_cloudwatch_logs.types.transformed_event_message


class TransformedLogRecord(TypedDict, closed=True):
    event_number: "capo_cloudwatch_logs.types.event_number.EventNumber"
    """<p>The event number.</p>"""
    event_message: NotRequired["capo_cloudwatch_logs.types.event_message.EventMessage"]
    """<p>The original log event message before it was transformed.</p>"""
    transformed_event_message: NotRequired[
        "capo_cloudwatch_logs.types.transformed_event_message.TransformedEventMessage"
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
    if data.get("eventNumber") is not None:
        out["event_number"] = data["eventNumber"]
    else:
        out["event_number"] = 0
    if data.get("eventMessage") is not None:
        out["event_message"] = data["eventMessage"]
    if data.get("transformedEventMessage") is not None:
        out["transformed_event_message"] = data["transformedEventMessage"]
    return out
