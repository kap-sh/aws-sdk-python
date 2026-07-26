"""Generated from Smithy shape ``com.amazonaws.mediapackage#ListOriginEndpointsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediapackage.types.__string
    import capo_mediapackage.types.max_results


class ListOriginEndpointsRequest(TypedDict, closed=True):
    channel_id: NotRequired["capo_mediapackage.types.__string.__string"]
    """When specified, the request will return only OriginEndpoints associated with the given Channel ID."""
    max_results: NotRequired["capo_mediapackage.types.max_results.MaxResults"]
    """The upper bound on the number of records to return."""
    next_token: NotRequired["capo_mediapackage.types.__string.__string"]
    """A token used to resume pagination from the end of a previous request."""


# --- restJson1 ser/de ---
def serialize_json(value: ListOriginEndpointsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListOriginEndpointsRequest:
    out: ListOriginEndpointsRequest = {}  # type: ignore[typeddict-item]
    return out
