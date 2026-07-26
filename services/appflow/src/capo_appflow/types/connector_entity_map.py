"""Generated from Smithy shape ``com.amazonaws.appflow#ConnectorEntityMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_appflow.types.connector_entity_list
    import capo_appflow.types.group

ConnectorEntityMap: TypeAlias = dict[
    "capo_appflow.types.group.Group",
    "capo_appflow.types.connector_entity_list.ConnectorEntityList",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: ConnectorEntityMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_appflow.types.connector_entity_list

        out[key] = capo_appflow.types.connector_entity_list.serialize_json(value)
    return out


def deserialize_json(data: dict) -> ConnectorEntityMap:
    out: ConnectorEntityMap = {}
    for key, value in data.items():
        import capo_appflow.types.connector_entity_list

        out[key] = capo_appflow.types.connector_entity_list.deserialize_json(value)
    return out
