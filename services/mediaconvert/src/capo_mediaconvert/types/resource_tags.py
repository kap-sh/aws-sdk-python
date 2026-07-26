"""Generated from Smithy shape ``com.amazonaws.mediaconvert#ResourceTags``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconvert.types.__map_of__string
    import capo_mediaconvert.types.__string


class ResourceTags(TypedDict, closed=True):
    arn: NotRequired["capo_mediaconvert.types.__string.__string"]
    """The Amazon Resource Name (ARN) of the resource."""
    tags: NotRequired["capo_mediaconvert.types.__map_of__string.__mapOf__string"]
    """The tags for the resource."""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceTags) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "tags" in value:
        import capo_mediaconvert.types.__map_of__string

        out["tags"] = capo_mediaconvert.types.__map_of__string.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> ResourceTags:
    out: ResourceTags = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "tags" in data:
        import capo_mediaconvert.types.__map_of__string

        out["tags"] = capo_mediaconvert.types.__map_of__string.deserialize_json(
            data["tags"]
        )
    return out
