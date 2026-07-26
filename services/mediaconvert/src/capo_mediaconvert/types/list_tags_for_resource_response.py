"""Generated from Smithy shape ``com.amazonaws.mediaconvert#ListTagsForResourceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconvert.types.resource_tags


class ListTagsForResourceResponse(TypedDict, closed=True):
    resource_tags: NotRequired["capo_mediaconvert.types.resource_tags.ResourceTags"]
    """The Amazon Resource Name (ARN) and tags for an AWS Elemental MediaConvert resource."""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceResponse) -> dict:
    out: dict = {}
    if "resource_tags" in value:
        import capo_mediaconvert.types.resource_tags

        out["resourceTags"] = capo_mediaconvert.types.resource_tags.serialize_json(
            value["resource_tags"]
        )
    return out


def deserialize_json(data: dict) -> ListTagsForResourceResponse:
    out: ListTagsForResourceResponse = {}  # type: ignore[typeddict-item]
    if "resourceTags" in data:
        import capo_mediaconvert.types.resource_tags

        out["resource_tags"] = capo_mediaconvert.types.resource_tags.deserialize_json(
            data["resourceTags"]
        )
    return out
