"""Generated from Smithy shape ``com.amazonaws.databrew#ListTagsForResourceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_databrew.types.tag_map


class ListTagsForResourceResponse(TypedDict, closed=True):
    tags: NotRequired["capo_databrew.types.tag_map.TagMap"]
    """<p>A list of tags associated with the DataBrew resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceResponse) -> dict:
    out: dict = {}
    if "tags" in value:
        import capo_databrew.types.tag_map

        out["Tags"] = capo_databrew.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> ListTagsForResourceResponse:
    out: ListTagsForResourceResponse = {}  # type: ignore[typeddict-item]
    if "Tags" in data:
        import capo_databrew.types.tag_map

        out["tags"] = capo_databrew.types.tag_map.deserialize_json(data["Tags"])
    return out
