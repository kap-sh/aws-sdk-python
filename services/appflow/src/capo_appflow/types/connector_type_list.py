"""Generated from Smithy shape ``com.amazonaws.appflow#ConnectorTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_appflow.types.connector_type

ConnectorTypeList: TypeAlias = list["capo_appflow.types.connector_type.ConnectorType"]


# --- restJson1 ser/de ---
def serialize_json(value: ConnectorTypeList) -> list:
    import capo_appflow.types.connector_type

    out: list = []
    for item in value:
        out.append(capo_appflow.types.connector_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> ConnectorTypeList:
    import capo_appflow.types.connector_type

    out: ConnectorTypeList = []
    for item in data:
        out.append(capo_appflow.types.connector_type.deserialize_json(item))
    return out
