"""Generated from Smithy shape ``com.amazonaws.iotevents#TransitionEvents``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot_events.types.transition_event

TransitionEvents: TypeAlias = list[
    "aws_sdk_iot_events.types.transition_event.TransitionEvent"
]


# --- restJson1 ser/de ---
def serialize_json(value: TransitionEvents) -> list:
    import aws_sdk_iot_events.types.transition_event

    out: list = []
    for item in value:
        out.append(aws_sdk_iot_events.types.transition_event.serialize_json(item))
    return out


def deserialize_json(data: list) -> TransitionEvents:
    import aws_sdk_iot_events.types.transition_event

    out: TransitionEvents = []
    for item in data:
        out.append(aws_sdk_iot_events.types.transition_event.deserialize_json(item))
    return out
