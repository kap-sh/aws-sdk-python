"""Generated from Smithy shape ``com.amazonaws.mediapackage#ListHarvestJobsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediapackage.types.__string
    import capo_mediapackage.types.max_results


class ListHarvestJobsRequest(TypedDict, closed=True):
    include_channel_id: NotRequired["capo_mediapackage.types.__string.__string"]
    """When specified, the request will return only HarvestJobs associated with the given Channel ID."""
    include_status: NotRequired["capo_mediapackage.types.__string.__string"]
    """When specified, the request will return only HarvestJobs in the given status."""
    max_results: NotRequired["capo_mediapackage.types.max_results.MaxResults"]
    """The upper bound on the number of records to return."""
    next_token: NotRequired["capo_mediapackage.types.__string.__string"]
    """A token used to resume pagination from the end of a previous request."""


# --- restJson1 ser/de ---
def serialize_json(value: ListHarvestJobsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListHarvestJobsRequest:
    out: ListHarvestJobsRequest = {}  # type: ignore[typeddict-item]
    return out
