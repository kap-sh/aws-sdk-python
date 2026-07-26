"""Generated from Smithy shape ``com.amazonaws.medialive#ListMultiplexesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__string
    import capo_medialive.types.max_results


class ListMultiplexesRequest(TypedDict, closed=True):
    max_results: NotRequired["capo_medialive.types.max_results.MaxResults"]
    """The maximum number of items to return."""
    next_token: NotRequired["capo_medialive.types.__string.__string"]
    """The token to retrieve the next page of results."""


# --- restJson1 ser/de ---
def serialize_json(value: ListMultiplexesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListMultiplexesRequest:
    out: ListMultiplexesRequest = {}  # type: ignore[typeddict-item]
    return out
