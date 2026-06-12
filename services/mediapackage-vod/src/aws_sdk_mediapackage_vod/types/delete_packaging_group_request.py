"""Generated from Smithy shape ``com.amazonaws.mediapackagevod#DeletePackagingGroupRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediapackage_vod.types.__string


class DeletePackagingGroupRequest(TypedDict):
    id: "aws_sdk_mediapackage_vod.types.__string.__string"
    """The ID of the MediaPackage VOD PackagingGroup resource to delete."""


# --- restJson1 ser/de ---
def serialize_json(value: DeletePackagingGroupRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeletePackagingGroupRequest:
    out: DeletePackagingGroupRequest = {}  # type: ignore[typeddict-item]
    return out
