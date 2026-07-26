"""Generated from Smithy shape ``com.amazonaws.iotevents#States``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot_events.types.state

States: TypeAlias = list["capo_iot_events.types.state.State"]


# --- restJson1 ser/de ---
def serialize_json(value: States) -> list:
    import capo_iot_events.types.state

    out: list = []
    for item in value:
        out.append(capo_iot_events.types.state.serialize_json(item))
    return out


def deserialize_json(data: list) -> States:
    import capo_iot_events.types.state

    out: States = []
    for item in data:
        out.append(capo_iot_events.types.state.deserialize_json(item))
    return out
