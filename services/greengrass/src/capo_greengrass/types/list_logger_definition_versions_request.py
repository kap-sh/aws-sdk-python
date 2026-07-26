"""Generated from Smithy shape ``com.amazonaws.greengrass#ListLoggerDefinitionVersionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_greengrass.types.__string


class ListLoggerDefinitionVersionsRequest(TypedDict, closed=True):
    logger_definition_id: "capo_greengrass.types.__string.__string"
    """The ID of the logger definition."""
    max_results: NotRequired["capo_greengrass.types.__string.__string"]
    """The maximum number of results to be returned per request."""
    next_token: NotRequired["capo_greengrass.types.__string.__string"]
    """The token for the next set of results, or ''null'' if there are no additional results."""


# --- restJson1 ser/de ---
def serialize_json(value: ListLoggerDefinitionVersionsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListLoggerDefinitionVersionsRequest:
    out: ListLoggerDefinitionVersionsRequest = {}  # type: ignore[typeddict-item]
    return out
