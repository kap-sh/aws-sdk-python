"""Generated from Smithy shape ``com.amazonaws.iotwireless#EventConfigurationsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot_wireless.types.event_configuration_item

EventConfigurationsList: TypeAlias = list[
    "capo_iot_wireless.types.event_configuration_item.EventConfigurationItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: EventConfigurationsList) -> list:
    import capo_iot_wireless.types.event_configuration_item

    out: list = []
    for item in value:
        out.append(
            capo_iot_wireless.types.event_configuration_item.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> EventConfigurationsList:
    import capo_iot_wireless.types.event_configuration_item

    out: EventConfigurationsList = []
    for item in data:
        out.append(
            capo_iot_wireless.types.event_configuration_item.deserialize_json(item)
        )
    return out
