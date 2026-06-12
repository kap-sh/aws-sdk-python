"""Generated from Smithy shape ``com.amazonaws.mediapackagevod#ListPackagingConfigurationsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediapackage_vod.types.__string
    import aws_sdk_mediapackage_vod.types.max_results


class ListPackagingConfigurationsRequest(TypedDict):
    max_results: NotRequired["aws_sdk_mediapackage_vod.types.max_results.MaxResults"]
    """Upper bound on number of records to return."""
    next_token: NotRequired["aws_sdk_mediapackage_vod.types.__string.__string"]
    """A token used to resume pagination from the end of a previous request."""
    packaging_group_id: NotRequired["aws_sdk_mediapackage_vod.types.__string.__string"]
    """Returns MediaPackage VOD PackagingConfigurations associated with the specified PackagingGroup."""


# --- restJson1 ser/de ---
def serialize_json(value: ListPackagingConfigurationsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListPackagingConfigurationsRequest:
    out: ListPackagingConfigurationsRequest = {}  # type: ignore[typeddict-item]
    return out
