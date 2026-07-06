"""Generated from Smithy shape ``com.amazonaws.mediapackagevod#DeleteAssetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediapackage_vod.types.__string


class DeleteAssetRequest(TypedDict, closed=True):
    id: "aws_sdk_mediapackage_vod.types.__string.__string"
    """The ID of the MediaPackage VOD Asset resource to delete."""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteAssetRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteAssetRequest:
    out: DeleteAssetRequest = {}  # type: ignore[typeddict-item]
    return out
