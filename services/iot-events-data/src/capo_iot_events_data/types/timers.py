"""Generated from Smithy shape ``com.amazonaws.ioteventsdata#Timers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot_events_data.types.timer

Timers: TypeAlias = list["capo_iot_events_data.types.timer.Timer"]


# --- restJson1 ser/de ---
def serialize_json(value: Timers) -> list:
    import capo_iot_events_data.types.timer

    out: list = []
    for item in value:
        out.append(capo_iot_events_data.types.timer.serialize_json(item))
    return out


def deserialize_json(data: list) -> Timers:
    import capo_iot_events_data.types.timer

    out: Timers = []
    for item in data:
        out.append(capo_iot_events_data.types.timer.deserialize_json(item))
    return out
