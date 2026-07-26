"""Generated from Smithy shape ``com.amazonaws.mediapackagevod#DescribePackagingGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mediapackage_vod.types.__string


class DescribePackagingGroupRequest(TypedDict, closed=True):
    id: "capo_mediapackage_vod.types.__string.__string"
    """The ID of a MediaPackage VOD PackagingGroup resource."""


# --- restJson1 ser/de ---
def serialize_json(value: DescribePackagingGroupRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribePackagingGroupRequest:
    out: DescribePackagingGroupRequest = {}  # type: ignore[typeddict-item]
    return out
