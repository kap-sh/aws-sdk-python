"""Generated from Smithy shape ``com.amazonaws.inspector#EventSubscription``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_inspector.errors import DeserializationError

if TYPE_CHECKING:
    import capo_inspector.types.inspector_event
    import capo_inspector.types.timestamp


class EventSubscription(TypedDict, closed=True):
    event: "capo_inspector.types.inspector_event.InspectorEvent"
    """<p>The event for which Amazon Simple Notification Service (SNS) notifications are sent.</p>"""
    subscribed_at: "capo_inspector.types.timestamp.Timestamp"
    """<p>The time at which <a>SubscribeToEvent</a> is called.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EventSubscription) -> dict:
    out: dict = {}
    import capo_inspector.types.inspector_event

    out["event"] = capo_inspector.types.inspector_event.serialize_aws_json_1_1(
        value["event"]
    )
    import capo_inspector.types.timestamp

    out["subscribedAt"] = capo_inspector.types.timestamp.serialize_aws_json_1_1(
        value["subscribed_at"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> EventSubscription:
    out: EventSubscription = {}  # type: ignore[typeddict-item]
    if "event" in data:
        import capo_inspector.types.inspector_event

        out["event"] = capo_inspector.types.inspector_event.deserialize_aws_json_1_1(
            data["event"]
        )
    else:
        raise DeserializationError("EventSubscription.event required")
    if "subscribedAt" in data:
        import capo_inspector.types.timestamp

        out["subscribed_at"] = capo_inspector.types.timestamp.deserialize_aws_json_1_1(
            data["subscribedAt"]
        )
    else:
        raise DeserializationError("EventSubscription.subscribed_at required")
    return out
