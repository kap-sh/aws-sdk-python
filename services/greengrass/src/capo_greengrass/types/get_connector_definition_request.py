"""Generated from Smithy shape ``com.amazonaws.greengrass#GetConnectorDefinitionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_greengrass.types.__string


class GetConnectorDefinitionRequest(TypedDict, closed=True):
    connector_definition_id: "capo_greengrass.types.__string.__string"
    """The ID of the connector definition."""


# --- restJson1 ser/de ---
def serialize_json(value: GetConnectorDefinitionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetConnectorDefinitionRequest:
    out: GetConnectorDefinitionRequest = {}  # type: ignore[typeddict-item]
    return out
