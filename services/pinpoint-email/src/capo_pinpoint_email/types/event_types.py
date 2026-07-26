"""Generated from Smithy shape ``com.amazonaws.pinpointemail#EventTypes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pinpoint_email.types.event_type

EventTypes: TypeAlias = list["capo_pinpoint_email.types.event_type.EventType"]


# --- restJson1 ser/de ---
def serialize_json(value: EventTypes) -> list:
    import capo_pinpoint_email.types.event_type

    out: list = []
    for item in value:
        out.append(capo_pinpoint_email.types.event_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> EventTypes:
    import capo_pinpoint_email.types.event_type

    out: EventTypes = []
    for item in data:
        out.append(capo_pinpoint_email.types.event_type.deserialize_json(item))
    return out
