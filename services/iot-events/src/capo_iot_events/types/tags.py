"""Generated from Smithy shape ``com.amazonaws.iotevents#Tags``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot_events.types.tag

Tags: TypeAlias = list["capo_iot_events.types.tag.Tag"]


# --- restJson1 ser/de ---
def serialize_json(value: Tags) -> list:
    import capo_iot_events.types.tag

    out: list = []
    for item in value:
        out.append(capo_iot_events.types.tag.serialize_json(item))
    return out


def deserialize_json(data: list) -> Tags:
    import capo_iot_events.types.tag

    out: Tags = []
    for item in data:
        out.append(capo_iot_events.types.tag.deserialize_json(item))
    return out
