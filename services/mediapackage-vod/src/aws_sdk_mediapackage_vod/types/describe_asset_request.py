"""Generated from Smithy shape ``com.amazonaws.mediapackagevod#DescribeAssetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediapackage_vod.types.__string


class DescribeAssetRequest(TypedDict, closed=True):
    id: "aws_sdk_mediapackage_vod.types.__string.__string"
    """The ID of an MediaPackage VOD Asset resource."""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeAssetRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeAssetRequest:
    out: DescribeAssetRequest = {}  # type: ignore[typeddict-item]
    return out
