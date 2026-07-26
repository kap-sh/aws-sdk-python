"""Generated from Smithy shape ``com.amazonaws.greengrass#ListConnectorDefinitionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_greengrass.types.__string


class ListConnectorDefinitionsRequest(TypedDict, closed=True):
    max_results: NotRequired["capo_greengrass.types.__string.__string"]
    """The maximum number of results to be returned per request."""
    next_token: NotRequired["capo_greengrass.types.__string.__string"]
    """The token for the next set of results, or ''null'' if there are no additional results."""


# --- restJson1 ser/de ---
def serialize_json(value: ListConnectorDefinitionsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListConnectorDefinitionsRequest:
    out: ListConnectorDefinitionsRequest = {}  # type: ignore[typeddict-item]
    return out
