"""Generated from Smithy shape ``com.amazonaws.mediaconvert#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconvert.types.__list_of__string
    import capo_mediaconvert.types.__string


class UntagResourceRequest(TypedDict, closed=True):
    arn: "capo_mediaconvert.types.__string.__string"
    """The Amazon Resource Name (ARN) of the resource that you want to remove tags from. To get the ARN, send a GET request with the resource name."""
    tag_keys: NotRequired["capo_mediaconvert.types.__list_of__string.__listOf__string"]
    """The keys of the tags that you want to remove from the resource."""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceRequest) -> dict:
    out: dict = {}
    if "tag_keys" in value:
        import capo_mediaconvert.types.__list_of__string

        out["tagKeys"] = capo_mediaconvert.types.__list_of__string.serialize_json(
            value["tag_keys"]
        )
    return out


def deserialize_json(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    if "tagKeys" in data:
        import capo_mediaconvert.types.__list_of__string

        out["tag_keys"] = capo_mediaconvert.types.__list_of__string.deserialize_json(
            data["tagKeys"]
        )
    return out
