"""Generated from Smithy shape ``com.amazonaws.ioteventsdata#TimerDefinitions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot_events_data.types.timer_definition

TimerDefinitions: TypeAlias = list[
    "capo_iot_events_data.types.timer_definition.TimerDefinition"
]


# --- restJson1 ser/de ---
def serialize_json(value: TimerDefinitions) -> list:
    import capo_iot_events_data.types.timer_definition

    out: list = []
    for item in value:
        out.append(capo_iot_events_data.types.timer_definition.serialize_json(item))
    return out


def deserialize_json(data: list) -> TimerDefinitions:
    import capo_iot_events_data.types.timer_definition

    out: TimerDefinitions = []
    for item in data:
        out.append(capo_iot_events_data.types.timer_definition.deserialize_json(item))
    return out
