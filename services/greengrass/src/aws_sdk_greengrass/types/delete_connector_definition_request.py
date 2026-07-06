"""Generated from Smithy shape ``com.amazonaws.greengrass#DeleteConnectorDefinitionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_greengrass.types.__string


class DeleteConnectorDefinitionRequest(TypedDict, closed=True):
    connector_definition_id: "aws_sdk_greengrass.types.__string.__string"
    """The ID of the connector definition."""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteConnectorDefinitionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteConnectorDefinitionRequest:
    out: DeleteConnectorDefinitionRequest = {}  # type: ignore[typeddict-item]
    return out
