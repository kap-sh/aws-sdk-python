"""Generated from Smithy shape ``com.amazonaws.greengrass#ListConnectorDefinitionVersionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_greengrass.types.__string


class ListConnectorDefinitionVersionsRequest(TypedDict, closed=True):
    connector_definition_id: "capo_greengrass.types.__string.__string"
    """The ID of the connector definition."""
    max_results: NotRequired["capo_greengrass.types.__string.__string"]
    """The maximum number of results to be returned per request."""
    next_token: NotRequired["capo_greengrass.types.__string.__string"]
    """The token for the next set of results, or ''null'' if there are no additional results."""


# --- restJson1 ser/de ---
def serialize_json(value: ListConnectorDefinitionVersionsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListConnectorDefinitionVersionsRequest:
    out: ListConnectorDefinitionVersionsRequest = {}  # type: ignore[typeddict-item]
    return out
