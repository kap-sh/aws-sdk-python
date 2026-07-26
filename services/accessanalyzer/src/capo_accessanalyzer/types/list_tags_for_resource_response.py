"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#ListTagsForResourceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_accessanalyzer.types.tags_map


class ListTagsForResourceResponse(TypedDict, closed=True):
    tags: NotRequired["capo_accessanalyzer.types.tags_map.TagsMap"]
    """<p>The tags that are applied to the specified resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceResponse) -> dict:
    out: dict = {}
    if "tags" in value:
        import capo_accessanalyzer.types.tags_map

        out["tags"] = capo_accessanalyzer.types.tags_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> ListTagsForResourceResponse:
    out: ListTagsForResourceResponse = {}  # type: ignore[typeddict-item]
    if "tags" in data:
        import capo_accessanalyzer.types.tags_map

        out["tags"] = capo_accessanalyzer.types.tags_map.deserialize_json(data["tags"])
    return out
