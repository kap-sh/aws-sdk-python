"""Generated from Smithy shape ``com.amazonaws.mediapackage#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediapackage.types.__map_of__string
    import capo_mediapackage.types.__string


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_mediapackage.types.__string.__string"
    tags: NotRequired["capo_mediapackage.types.__map_of__string.__mapOf__string"]


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    if "tags" in value:
        import capo_mediapackage.types.__map_of__string

        out["tags"] = capo_mediapackage.types.__map_of__string.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if "tags" in data:
        import capo_mediapackage.types.__map_of__string

        out["tags"] = capo_mediapackage.types.__map_of__string.deserialize_json(
            data["tags"]
        )
    return out
