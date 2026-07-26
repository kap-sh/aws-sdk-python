"""Generated from Smithy shape ``com.amazonaws.mediapackagevod#ListPackagingGroupsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediapackage_vod.types.__string
    import capo_mediapackage_vod.types.max_results


class ListPackagingGroupsRequest(TypedDict, closed=True):
    max_results: NotRequired["capo_mediapackage_vod.types.max_results.MaxResults"]
    """Upper bound on number of records to return."""
    next_token: NotRequired["capo_mediapackage_vod.types.__string.__string"]
    """A token used to resume pagination from the end of a previous request."""


# --- restJson1 ser/de ---
def serialize_json(value: ListPackagingGroupsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListPackagingGroupsRequest:
    out: ListPackagingGroupsRequest = {}  # type: ignore[typeddict-item]
    return out
