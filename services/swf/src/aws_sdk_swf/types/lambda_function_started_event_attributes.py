"""Generated from Smithy shape ``com.amazonaws.swf#LambdaFunctionStartedEventAttributes``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_swf.types.event_id


class LambdaFunctionStartedEventAttributes(TypedDict):
    scheduled_event_id: "aws_sdk_swf.types.event_id.EventId"
    """<p>The ID of the <code>LambdaFunctionScheduled</code> event that was recorded when this activity task was scheduled. To help diagnose issues, use this information to trace back the chain of events leading up to this event.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LambdaFunctionStartedEventAttributes) -> dict:
    out: dict = {}
    out["scheduledEventId"] = value.get("scheduled_event_id", 0)
    return out


def deserialize_aws_json_1_0(data: dict) -> LambdaFunctionStartedEventAttributes:
    out: LambdaFunctionStartedEventAttributes = {}  # type: ignore[typeddict-item]
    if "scheduledEventId" in data:
        out["scheduled_event_id"] = data["scheduledEventId"]
    else:
        out["scheduled_event_id"] = 0
    return out
