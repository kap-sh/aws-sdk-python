"""Generated from Smithy shape ``com.amazonaws.xray#ListTagsForResourceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_xray.types.string
    import capo_xray.types.tag_list


class ListTagsForResourceResponse(TypedDict, closed=True):
    tags: NotRequired["capo_xray.types.tag_list.TagList"]
    """<p>A list of tags, as key and value pairs, that is associated with the specified X-Ray group or sampling rule.</p>"""
    next_token: NotRequired["capo_xray.types.string.String"]
    """<p>A pagination token. If multiple pages of results are returned, use the <code>NextToken</code> value returned with the current page of results to get the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceResponse) -> dict:
    out: dict = {}
    if "tags" in value:
        import capo_xray.types.tag_list

        out["Tags"] = capo_xray.types.tag_list.serialize_json(value["tags"])
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListTagsForResourceResponse:
    out: ListTagsForResourceResponse = {}  # type: ignore[typeddict-item]
    if "Tags" in data:
        import capo_xray.types.tag_list

        out["tags"] = capo_xray.types.tag_list.deserialize_json(data["Tags"])
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
