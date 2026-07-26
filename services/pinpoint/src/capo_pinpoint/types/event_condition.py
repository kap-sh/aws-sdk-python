"""Generated from Smithy shape ``com.amazonaws.pinpoint#EventCondition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.__string
    import capo_pinpoint.types.event_dimensions


class EventCondition(TypedDict, closed=True):
    dimensions: NotRequired["capo_pinpoint.types.event_dimensions.EventDimensions"]
    """<p>The dimensions for the event filter to use for the activity.</p>"""
    message_activity: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The message identifier (message_id) for the message to use when determining whether message events meet the condition.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EventCondition) -> dict:
    out: dict = {}
    if "dimensions" in value:
        import capo_pinpoint.types.event_dimensions

        out["Dimensions"] = capo_pinpoint.types.event_dimensions.serialize_json(
            value["dimensions"]
        )
    if "message_activity" in value:
        out["MessageActivity"] = value["message_activity"]
    return out


def deserialize_json(data: dict) -> EventCondition:
    out: EventCondition = {}  # type: ignore[typeddict-item]
    if "Dimensions" in data:
        import capo_pinpoint.types.event_dimensions

        out["dimensions"] = capo_pinpoint.types.event_dimensions.deserialize_json(
            data["Dimensions"]
        )
    if "MessageActivity" in data:
        out["message_activity"] = data["MessageActivity"]
    return out
