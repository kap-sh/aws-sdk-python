"""Generated from Smithy shape ``com.amazonaws.detective#ListTagsForResourceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_detective.types.tag_map


class ListTagsForResourceResponse(TypedDict, closed=True):
    tags: NotRequired["capo_detective.types.tag_map.TagMap"]
    """<p>The tag values that are assigned to the behavior graph. The request returns up to 50 tag values.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceResponse) -> dict:
    out: dict = {}
    if "tags" in value:
        import capo_detective.types.tag_map

        out["Tags"] = capo_detective.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> ListTagsForResourceResponse:
    out: ListTagsForResourceResponse = {}  # type: ignore[typeddict-item]
    if "Tags" in data:
        import capo_detective.types.tag_map

        out["tags"] = capo_detective.types.tag_map.deserialize_json(data["Tags"])
    return out
