"""Generated from Smithy shape ``com.amazonaws.ioteventsdata#Messages``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot_events_data.types.message

Messages: TypeAlias = list["capo_iot_events_data.types.message.Message"]


# --- restJson1 ser/de ---
def serialize_json(value: Messages) -> list:
    import capo_iot_events_data.types.message

    out: list = []
    for item in value:
        out.append(capo_iot_events_data.types.message.serialize_json(item))
    return out


def deserialize_json(data: list) -> Messages:
    import capo_iot_events_data.types.message

    out: Messages = []
    for item in data:
        out.append(capo_iot_events_data.types.message.deserialize_json(item))
    return out
