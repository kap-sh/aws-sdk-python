"""Generated from Smithy shape ``com.amazonaws.greengrass#Connector``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_greengrass.types.__map_of__string
    import aws_sdk_greengrass.types.__string


class Connector(TypedDict):
    connector_arn: NotRequired["aws_sdk_greengrass.types.__string.__string"]
    """The ARN of the connector."""
    id: NotRequired["aws_sdk_greengrass.types.__string.__string"]
    """A descriptive or arbitrary ID for the connector. This value must be unique within the connector definition version. Max length is 128 characters with pattern [a-zA-Z0-9:_-]+."""
    parameters: NotRequired["aws_sdk_greengrass.types.__map_of__string.__mapOf__string"]
    """The parameters or configuration that the connector uses."""


# --- restJson1 ser/de ---
def serialize_json(value: Connector) -> dict:
    out: dict = {}
    if "connector_arn" in value:
        out["ConnectorArn"] = value["connector_arn"]
    if "id" in value:
        out["Id"] = value["id"]
    if "parameters" in value:
        import aws_sdk_greengrass.types.__map_of__string

        out["Parameters"] = aws_sdk_greengrass.types.__map_of__string.serialize_json(
            value["parameters"]
        )
    return out


def deserialize_json(data: dict) -> Connector:
    out: Connector = {}  # type: ignore[typeddict-item]
    if "ConnectorArn" in data:
        out["connector_arn"] = data["ConnectorArn"]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Parameters" in data:
        import aws_sdk_greengrass.types.__map_of__string

        out["parameters"] = aws_sdk_greengrass.types.__map_of__string.deserialize_json(
            data["Parameters"]
        )
    return out
