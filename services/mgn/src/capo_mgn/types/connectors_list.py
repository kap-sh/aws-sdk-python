"""Generated from Smithy shape ``com.amazonaws.mgn#ConnectorsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mgn.types.connector

ConnectorsList: TypeAlias = list["capo_mgn.types.connector.Connector"]


# --- restJson1 ser/de ---
def serialize_json(value: ConnectorsList) -> list:
    import capo_mgn.types.connector

    out: list = []
    for item in value:
        out.append(capo_mgn.types.connector.serialize_json(item))
    return out


def deserialize_json(data: list) -> ConnectorsList:
    import capo_mgn.types.connector

    out: ConnectorsList = []
    for item in data:
        out.append(capo_mgn.types.connector.deserialize_json(item))
    return out
