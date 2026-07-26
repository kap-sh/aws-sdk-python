"""Generated from Smithy shape ``com.amazonaws.swf#DecisionTaskStartedEventAttributes``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_swf.types.event_id
    import capo_swf.types.identity


class DecisionTaskStartedEventAttributes(TypedDict, closed=True):
    identity: NotRequired["capo_swf.types.identity.Identity"]
    """<p>Identity of the decider making the request. This enables diagnostic tracing when problems arise. The form of this identity is user defined.</p>"""
    scheduled_event_id: "capo_swf.types.event_id.EventId"
    """<p>The ID of the <code>DecisionTaskScheduled</code> event that was recorded when this decision task was scheduled. This information can be useful for diagnosing problems by tracing back the chain of events leading up to this event.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DecisionTaskStartedEventAttributes) -> dict:
    out: dict = {}
    if "identity" in value:
        out["identity"] = value["identity"]
    out["scheduledEventId"] = value.get("scheduled_event_id", 0)
    return out


def deserialize_aws_json_1_0(data: dict) -> DecisionTaskStartedEventAttributes:
    out: DecisionTaskStartedEventAttributes = {}  # type: ignore[typeddict-item]
    if "identity" in data:
        out["identity"] = data["identity"]
    if "scheduledEventId" in data:
        out["scheduled_event_id"] = data["scheduledEventId"]
    else:
        out["scheduled_event_id"] = 0
    return out
