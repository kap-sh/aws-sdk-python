"""Generated from Smithy shape ``com.amazonaws.greengrass#CreateConnectorDefinitionVersionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_greengrass.types.__list_of_connector
    import aws_sdk_greengrass.types.__string


class CreateConnectorDefinitionVersionRequest(TypedDict, closed=True):
    amzn_client_token: NotRequired["aws_sdk_greengrass.types.__string.__string"]
    """A client token used to correlate requests and responses."""
    connector_definition_id: "aws_sdk_greengrass.types.__string.__string"
    """The ID of the connector definition."""
    connectors: NotRequired[
        "aws_sdk_greengrass.types.__list_of_connector.__listOfConnector"
    ]
    """A list of references to connectors in this version, with their corresponding configuration settings."""


# --- restJson1 ser/de ---
def serialize_json(value: CreateConnectorDefinitionVersionRequest) -> dict:
    out: dict = {}
    if "connectors" in value:
        import aws_sdk_greengrass.types.__list_of_connector

        out["Connectors"] = aws_sdk_greengrass.types.__list_of_connector.serialize_json(
            value["connectors"]
        )
    return out


def deserialize_json(data: dict) -> CreateConnectorDefinitionVersionRequest:
    out: CreateConnectorDefinitionVersionRequest = {}  # type: ignore[typeddict-item]
    if "Connectors" in data:
        import aws_sdk_greengrass.types.__list_of_connector

        out["connectors"] = (
            aws_sdk_greengrass.types.__list_of_connector.deserialize_json(
                data["Connectors"]
            )
        )
    return out
