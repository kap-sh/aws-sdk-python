"""Generated from Smithy shape ``com.amazonaws.swf#ActivityTaskCanceledEventAttributes``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_swf.types.data
    import capo_swf.types.event_id


class ActivityTaskCanceledEventAttributes(TypedDict, closed=True):
    details: NotRequired["capo_swf.types.data.Data"]
    """<p>Details of the cancellation.</p>"""
    scheduled_event_id: "capo_swf.types.event_id.EventId"
    """<p>The ID of the <code>ActivityTaskScheduled</code> event that was recorded when this activity task was scheduled. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.</p>"""
    started_event_id: "capo_swf.types.event_id.EventId"
    """<p>The ID of the <code>ActivityTaskStarted</code> event recorded when this activity task was started. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.</p>"""
    latest_cancel_requested_event_id: "capo_swf.types.event_id.EventId"
    """<p>If set, contains the ID of the last <code>ActivityTaskCancelRequested</code> event recorded for this activity task. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ActivityTaskCanceledEventAttributes) -> dict:
    out: dict = {}
    if "details" in value:
        out["details"] = value["details"]
    out["scheduledEventId"] = value.get("scheduled_event_id", 0)
    out["startedEventId"] = value.get("started_event_id", 0)
    out["latestCancelRequestedEventId"] = value.get(
        "latest_cancel_requested_event_id", 0
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ActivityTaskCanceledEventAttributes:
    out: ActivityTaskCanceledEventAttributes = {}  # type: ignore[typeddict-item]
    if "details" in data:
        out["details"] = data["details"]
    if "scheduledEventId" in data:
        out["scheduled_event_id"] = data["scheduledEventId"]
    else:
        out["scheduled_event_id"] = 0
    if "startedEventId" in data:
        out["started_event_id"] = data["startedEventId"]
    else:
        out["started_event_id"] = 0
    if "latestCancelRequestedEventId" in data:
        out["latest_cancel_requested_event_id"] = data["latestCancelRequestedEventId"]
    else:
        out["latest_cancel_requested_event_id"] = 0
    return out
