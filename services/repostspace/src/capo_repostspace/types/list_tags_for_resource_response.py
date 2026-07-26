"""Generated from Smithy shape ``com.amazonaws.repostspace#ListTagsForResourceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_repostspace.types.tags


class ListTagsForResourceResponse(TypedDict, closed=True):
    tags: NotRequired["capo_repostspace.types.tags.Tags"]
    """<p>The list of tags that are associated with the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceResponse) -> dict:
    out: dict = {}
    if "tags" in value:
        import capo_repostspace.types.tags

        out["tags"] = capo_repostspace.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> ListTagsForResourceResponse:
    out: ListTagsForResourceResponse = {}  # type: ignore[typeddict-item]
    if "tags" in data:
        import capo_repostspace.types.tags

        out["tags"] = capo_repostspace.types.tags.deserialize_json(data["tags"])
    return out
