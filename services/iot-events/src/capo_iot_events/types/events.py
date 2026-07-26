"""Generated from Smithy shape ``com.amazonaws.iotevents#Events``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot_events.types.event

Events: TypeAlias = list["capo_iot_events.types.event.Event"]


# --- restJson1 ser/de ---
def serialize_json(value: Events) -> list:
    import capo_iot_events.types.event

    out: list = []
    for item in value:
        out.append(capo_iot_events.types.event.serialize_json(item))
    return out


def deserialize_json(data: list) -> Events:
    import capo_iot_events.types.event

    out: Events = []
    for item in data:
        out.append(capo_iot_events.types.event.deserialize_json(item))
    return out
