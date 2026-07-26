"""Generated from Smithy shape ``com.amazonaws.appflow#ConnectorEntityFieldList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_appflow.types.connector_entity_field

ConnectorEntityFieldList: TypeAlias = list[
    "capo_appflow.types.connector_entity_field.ConnectorEntityField"
]


# --- restJson1 ser/de ---
def serialize_json(value: ConnectorEntityFieldList) -> list:
    import capo_appflow.types.connector_entity_field

    out: list = []
    for item in value:
        out.append(capo_appflow.types.connector_entity_field.serialize_json(item))
    return out


def deserialize_json(data: list) -> ConnectorEntityFieldList:
    import capo_appflow.types.connector_entity_field

    out: ConnectorEntityFieldList = []
    for item in data:
        out.append(capo_appflow.types.connector_entity_field.deserialize_json(item))
    return out
