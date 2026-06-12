"""Generated from Smithy shape ``com.amazonaws.swf#MarkerRecordedEventAttributes``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_swf.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_swf.types.data
    import aws_sdk_swf.types.event_id
    import aws_sdk_swf.types.marker_name


class MarkerRecordedEventAttributes(TypedDict):
    marker_name: "aws_sdk_swf.types.marker_name.MarkerName"
    """<p>The name of the marker.</p>"""
    details: NotRequired["aws_sdk_swf.types.data.Data"]
    """<p>The details of the marker.</p>"""
    decision_task_completed_event_id: "aws_sdk_swf.types.event_id.EventId"
    """<p>The ID of the <code>DecisionTaskCompleted</code> event corresponding to the decision task that resulted in the <code>RecordMarker</code> decision that requested this marker. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: MarkerRecordedEventAttributes) -> dict:
    out: dict = {}
    out["markerName"] = value["marker_name"]
    if "details" in value:
        out["details"] = value["details"]
    out["decisionTaskCompletedEventId"] = value.get(
        "decision_task_completed_event_id", 0
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> MarkerRecordedEventAttributes:
    out: MarkerRecordedEventAttributes = {}  # type: ignore[typeddict-item]
    if "markerName" in data:
        out["marker_name"] = data["markerName"]
    else:
        raise DeserializationError("MarkerRecordedEventAttributes.marker_name required")
    if "details" in data:
        out["details"] = data["details"]
    if "decisionTaskCompletedEventId" in data:
        out["decision_task_completed_event_id"] = data["decisionTaskCompletedEventId"]
    else:
        out["decision_task_completed_event_id"] = 0
    return out
