"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#ListTagsForResourceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iottwinmaker.types.next_token
    import capo_iottwinmaker.types.tag_map


class ListTagsForResourceResponse(TypedDict, closed=True):
    tags: NotRequired["capo_iottwinmaker.types.tag_map.TagMap"]
    """<p>Metadata that you can use to manage a resource.</p>"""
    next_token: NotRequired["capo_iottwinmaker.types.next_token.NextToken"]
    """<p>The string that specifies the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceResponse) -> dict:
    out: dict = {}
    if "tags" in value:
        import capo_iottwinmaker.types.tag_map

        out["tags"] = capo_iottwinmaker.types.tag_map.serialize_json(value["tags"])
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListTagsForResourceResponse:
    out: ListTagsForResourceResponse = {}  # type: ignore[typeddict-item]
    if "tags" in data:
        import capo_iottwinmaker.types.tag_map

        out["tags"] = capo_iottwinmaker.types.tag_map.deserialize_json(data["tags"])
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
