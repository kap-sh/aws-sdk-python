"""Generated from Smithy shape ``com.amazonaws.iotevents#Events``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot_events.types.event

Events: TypeAlias = list["aws_sdk_iot_events.types.event.Event"]


# --- restJson1 ser/de ---
def serialize_json(value: Events) -> list:
    import aws_sdk_iot_events.types.event

    out: list = []
    for item in value:
        out.append(aws_sdk_iot_events.types.event.serialize_json(item))
    return out


def deserialize_json(data: list) -> Events:
    import aws_sdk_iot_events.types.event

    out: Events = []
    for item in data:
        out.append(aws_sdk_iot_events.types.event.deserialize_json(item))
    return out
