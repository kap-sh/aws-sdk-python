"""Generated from Smithy shape ``com.amazonaws.iot#EventConfigurations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot.types.configuration
    import capo_iot.types.event_type

EventConfigurations: TypeAlias = dict[
    "capo_iot.types.event_type.EventType", "capo_iot.types.configuration.Configuration"
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: EventConfigurations) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_iot.types.configuration
        import capo_iot.types.event_type

        out[capo_iot.types.event_type.serialize_json(key)] = (
            capo_iot.types.configuration.serialize_json(value)
        )
    return out


def deserialize_json(data: dict) -> EventConfigurations:
    out: EventConfigurations = {}
    for key, value in data.items():
        import capo_iot.types.configuration
        import capo_iot.types.event_type

        out[capo_iot.types.event_type.deserialize_json(key)] = (
            capo_iot.types.configuration.deserialize_json(value)
        )
    return out
