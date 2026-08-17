"""Generated from Smithy shape ``com.amazonaws.lambda#EventSourceMappingsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lambda.types.event_source_mapping_configuration

EventSourceMappingsList: TypeAlias = list[
    "capo_lambda.types.event_source_mapping_configuration.EventSourceMappingConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: EventSourceMappingsList) -> list:
    import capo_lambda.types.event_source_mapping_configuration

    out: list = []
    for item in value:
        out.append(
            capo_lambda.types.event_source_mapping_configuration.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> EventSourceMappingsList:
    import capo_lambda.types.event_source_mapping_configuration

    out: EventSourceMappingsList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_lambda.types.event_source_mapping_configuration.deserialize_json(item)
        )
    return out
