"""Generated from Smithy shape ``com.amazonaws.sesv2#EventTypes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sesv2.types.event_type

EventTypes: TypeAlias = list["capo_sesv2.types.event_type.EventType"]


# --- restJson1 ser/de ---
def serialize_json(value: EventTypes) -> list:
    import capo_sesv2.types.event_type

    out: list = []
    for item in value:
        out.append(capo_sesv2.types.event_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> EventTypes:
    import capo_sesv2.types.event_type

    out: EventTypes = []
    for item in data:
        out.append(capo_sesv2.types.event_type.deserialize_json(item))
    return out
