"""Generated from Smithy shape ``com.amazonaws.swf#LambdaFunctionFailedEventAttributes``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_swf.types.data
    import capo_swf.types.event_id
    import capo_swf.types.failure_reason


class LambdaFunctionFailedEventAttributes(TypedDict, closed=True):
    scheduled_event_id: "capo_swf.types.event_id.EventId"
    """<p>The ID of the <code>LambdaFunctionScheduled</code> event that was recorded when this activity task was scheduled. To help diagnose issues, use this information to trace back the chain of events leading up to this event.</p>"""
    started_event_id: "capo_swf.types.event_id.EventId"
    """<p>The ID of the <code>LambdaFunctionStarted</code> event recorded when this activity task started. To help diagnose issues, use this information to trace back the chain of events leading up to this event.</p>"""
    reason: NotRequired["capo_swf.types.failure_reason.FailureReason"]
    """<p>The reason provided for the failure.</p>"""
    details: NotRequired["capo_swf.types.data.Data"]
    """<p>The details of the failure.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LambdaFunctionFailedEventAttributes) -> dict:
    out: dict = {}
    out["scheduledEventId"] = value.get("scheduled_event_id", 0)
    out["startedEventId"] = value.get("started_event_id", 0)
    if "reason" in value:
        out["reason"] = value["reason"]
    if "details" in value:
        out["details"] = value["details"]
    return out


def deserialize_aws_json_1_0(data: dict) -> LambdaFunctionFailedEventAttributes:
    out: LambdaFunctionFailedEventAttributes = {}  # type: ignore[typeddict-item]
    if "scheduledEventId" in data:
        out["scheduled_event_id"] = data["scheduledEventId"]
    else:
        out["scheduled_event_id"] = 0
    if "startedEventId" in data:
        out["started_event_id"] = data["startedEventId"]
    else:
        out["started_event_id"] = 0
    if "reason" in data:
        out["reason"] = data["reason"]
    if "details" in data:
        out["details"] = data["details"]
    return out
