"""Generated from Smithy shape ``com.amazonaws.mgn#ConnectorsList``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_mgn.types.connector

ConnectorsList: TypeAlias = list["aws_sdk_mgn.types.connector.Connector"]


# --- restJson1 ser/de ---
def serialize_json(value: ConnectorsList) -> list:
    import aws_sdk_mgn.types.connector
    out: list = []
    for item in value:
        out.append(aws_sdk_mgn.types.connector.serialize_json(item))
    return out


def deserialize_json(data: list) -> ConnectorsList:
    import aws_sdk_mgn.types.connector
    out: ConnectorsList = []
    for item in data:
        out.append(aws_sdk_mgn.types.connector.deserialize_json(item))
    return out