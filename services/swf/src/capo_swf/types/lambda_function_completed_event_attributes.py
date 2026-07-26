"""Generated from Smithy shape ``com.amazonaws.swf#LambdaFunctionCompletedEventAttributes``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_swf.types.data
    import capo_swf.types.event_id


class LambdaFunctionCompletedEventAttributes(TypedDict, closed=True):
    scheduled_event_id: "capo_swf.types.event_id.EventId"
    """<p>The ID of the <code>LambdaFunctionScheduled</code> event that was recorded when this Lambda task was scheduled. To help diagnose issues, use this information to trace back the chain of events leading up to this event.</p>"""
    started_event_id: "capo_swf.types.event_id.EventId"
    """<p>The ID of the <code>LambdaFunctionStarted</code> event recorded when this activity task started. To help diagnose issues, use this information to trace back the chain of events leading up to this event.</p>"""
    result: NotRequired["capo_swf.types.data.Data"]
    """<p>The results of the Lambda task.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LambdaFunctionCompletedEventAttributes) -> dict:
    out: dict = {}
    out["scheduledEventId"] = value.get("scheduled_event_id", 0)
    out["startedEventId"] = value.get("started_event_id", 0)
    if "result" in value:
        out["result"] = value["result"]
    return out


def deserialize_aws_json_1_0(data: dict) -> LambdaFunctionCompletedEventAttributes:
    out: LambdaFunctionCompletedEventAttributes = {}  # type: ignore[typeddict-item]
    if "scheduledEventId" in data:
        out["scheduled_event_id"] = data["scheduledEventId"]
    else:
        out["scheduled_event_id"] = 0
    if "startedEventId" in data:
        out["started_event_id"] = data["startedEventId"]
    else:
        out["started_event_id"] = 0
    if "result" in data:
        out["result"] = data["result"]
    return out
