"""Generated from Smithy shape ``com.amazonaws.greengrass#ConnectorDefinitionVersion``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_greengrass.types.__list_of_connector


class ConnectorDefinitionVersion(TypedDict, closed=True):
    connectors: NotRequired[
        "aws_sdk_greengrass.types.__list_of_connector.__listOfConnector"
    ]
    """A list of references to connectors in this version, with their corresponding configuration settings."""


# --- restJson1 ser/de ---
def serialize_json(value: ConnectorDefinitionVersion) -> dict:
    out: dict = {}
    if "connectors" in value:
        import aws_sdk_greengrass.types.__list_of_connector

        out["Connectors"] = aws_sdk_greengrass.types.__list_of_connector.serialize_json(
            value["connectors"]
        )
    return out


def deserialize_json(data: dict) -> ConnectorDefinitionVersion:
    out: ConnectorDefinitionVersion = {}  # type: ignore[typeddict-item]
    if "Connectors" in data:
        import aws_sdk_greengrass.types.__list_of_connector

        out["connectors"] = (
            aws_sdk_greengrass.types.__list_of_connector.deserialize_json(
                data["Connectors"]
            )
        )
    return out
