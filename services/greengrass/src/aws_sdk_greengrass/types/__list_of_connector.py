"""Generated from Smithy shape ``com.amazonaws.greengrass#__listOfConnector``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_greengrass.types.connector

__listOfConnector: TypeAlias = list["aws_sdk_greengrass.types.connector.Connector"]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfConnector) -> list:
    import aws_sdk_greengrass.types.connector

    out: list = []
    for item in value:
        out.append(aws_sdk_greengrass.types.connector.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfConnector:
    import aws_sdk_greengrass.types.connector

    out: __listOfConnector = []
    for item in data:
        out.append(aws_sdk_greengrass.types.connector.deserialize_json(item))
    return out
