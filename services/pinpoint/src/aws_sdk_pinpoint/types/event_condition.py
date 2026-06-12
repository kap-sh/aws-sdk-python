"""Generated from Smithy shape ``com.amazonaws.pinpoint#EventCondition``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.__string
    import aws_sdk_pinpoint.types.event_dimensions


class EventCondition(TypedDict):
    dimensions: NotRequired["aws_sdk_pinpoint.types.event_dimensions.EventDimensions"]
    """<p>The dimensions for the event filter to use for the activity.</p>"""
    message_activity: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The message identifier (message_id) for the message to use when determining whether message events meet the condition.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EventCondition) -> dict:
    out: dict = {}
    if "dimensions" in value:
        import aws_sdk_pinpoint.types.event_dimensions

        out["Dimensions"] = aws_sdk_pinpoint.types.event_dimensions.serialize_json(
            value["dimensions"]
        )
    if "message_activity" in value:
        out["MessageActivity"] = value["message_activity"]
    return out


def deserialize_json(data: dict) -> EventCondition:
    out: EventCondition = {}  # type: ignore[typeddict-item]
    if "Dimensions" in data:
        import aws_sdk_pinpoint.types.event_dimensions

        out["dimensions"] = aws_sdk_pinpoint.types.event_dimensions.deserialize_json(
            data["Dimensions"]
        )
    if "MessageActivity" in data:
        out["message_activity"] = data["MessageActivity"]
    return out
