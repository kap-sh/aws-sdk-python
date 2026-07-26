"""Generated from Smithy shape ``com.amazonaws.iot#ListTagsForResourceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.next_token
    import capo_iot.types.tag_list


class ListTagsForResourceResponse(TypedDict, closed=True):
    tags: NotRequired["capo_iot.types.tag_list.TagList"]
    """<p>The list of tags assigned to the resource.</p>"""
    next_token: NotRequired["capo_iot.types.next_token.NextToken"]
    """<p>The token to use to get the next set of results, or <b>null</b> if there are no additional results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceResponse) -> dict:
    out: dict = {}
    if "tags" in value:
        import capo_iot.types.tag_list

        out["tags"] = capo_iot.types.tag_list.serialize_json(value["tags"])
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListTagsForResourceResponse:
    out: ListTagsForResourceResponse = {}  # type: ignore[typeddict-item]
    if "tags" in data:
        import capo_iot.types.tag_list

        out["tags"] = capo_iot.types.tag_list.deserialize_json(data["tags"])
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
