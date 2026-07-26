"""Generated from Smithy shape ``com.amazonaws.mediapackagevod#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediapackage_vod.types.__map_of__string
    import capo_mediapackage_vod.types.__string


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_mediapackage_vod.types.__string.__string"
    """The Amazon Resource Name (ARN) for the resource. You can get this from the response to any request to the resource."""
    tags: NotRequired["capo_mediapackage_vod.types.__map_of__string.__mapOf__string"]
    """A collection of tags associated with a resource"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    if "tags" in value:
        import capo_mediapackage_vod.types.__map_of__string

        out["tags"] = capo_mediapackage_vod.types.__map_of__string.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if "tags" in data:
        import capo_mediapackage_vod.types.__map_of__string

        out["tags"] = capo_mediapackage_vod.types.__map_of__string.deserialize_json(
            data["tags"]
        )
    return out
