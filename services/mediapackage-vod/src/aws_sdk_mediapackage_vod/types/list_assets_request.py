"""Generated from Smithy shape ``com.amazonaws.mediapackagevod#ListAssetsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediapackage_vod.types.__string
    import aws_sdk_mediapackage_vod.types.max_results


class ListAssetsRequest(TypedDict, closed=True):
    max_results: NotRequired["aws_sdk_mediapackage_vod.types.max_results.MaxResults"]
    """Upper bound on number of records to return."""
    next_token: NotRequired["aws_sdk_mediapackage_vod.types.__string.__string"]
    """A token used to resume pagination from the end of a previous request."""
    packaging_group_id: NotRequired["aws_sdk_mediapackage_vod.types.__string.__string"]
    """Returns Assets associated with the specified PackagingGroup."""


# --- restJson1 ser/de ---
def serialize_json(value: ListAssetsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListAssetsRequest:
    out: ListAssetsRequest = {}  # type: ignore[typeddict-item]
    return out
