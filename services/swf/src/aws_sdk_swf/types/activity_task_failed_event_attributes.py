"""Generated from Smithy shape ``com.amazonaws.swf#ActivityTaskFailedEventAttributes``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_swf.types.data
    import aws_sdk_swf.types.event_id
    import aws_sdk_swf.types.failure_reason


class ActivityTaskFailedEventAttributes(TypedDict):
    reason: NotRequired["aws_sdk_swf.types.failure_reason.FailureReason"]
    """<p>The reason provided for the failure.</p>"""
    details: NotRequired["aws_sdk_swf.types.data.Data"]
    """<p>The details of the failure.</p>"""
    scheduled_event_id: "aws_sdk_swf.types.event_id.EventId"
    """<p>The ID of the <code>ActivityTaskScheduled</code> event that was recorded when this activity task was scheduled. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.</p>"""
    started_event_id: "aws_sdk_swf.types.event_id.EventId"
    """<p>The ID of the <code>ActivityTaskStarted</code> event recorded when this activity task was started. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ActivityTaskFailedEventAttributes) -> dict:
    out: dict = {}
    if "reason" in value:
        out["reason"] = value["reason"]
    if "details" in value:
        out["details"] = value["details"]
    out["scheduledEventId"] = value.get("scheduled_event_id", 0)
    out["startedEventId"] = value.get("started_event_id", 0)
    return out


def deserialize_aws_json_1_0(data: dict) -> ActivityTaskFailedEventAttributes:
    out: ActivityTaskFailedEventAttributes = {}  # type: ignore[typeddict-item]
    if "reason" in data:
        out["reason"] = data["reason"]
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
    return out
