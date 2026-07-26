"""Generated from Smithy shape ``com.amazonaws.clouddirectory#ListTagsForResourceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_clouddirectory.types.next_token
    import capo_clouddirectory.types.tag_list


class ListTagsForResourceResponse(TypedDict, closed=True):
    tags: NotRequired["capo_clouddirectory.types.tag_list.TagList"]
    """<p>A list of tag key value pairs that are associated with the response.</p>"""
    next_token: NotRequired["capo_clouddirectory.types.next_token.NextToken"]
    """<p>The token to use to retrieve the next page of results. This value is null when there are no more results to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceResponse) -> dict:
    out: dict = {}
    if "tags" in value:
        import capo_clouddirectory.types.tag_list

        out["Tags"] = capo_clouddirectory.types.tag_list.serialize_json(value["tags"])
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListTagsForResourceResponse:
    out: ListTagsForResourceResponse = {}  # type: ignore[typeddict-item]
    if "Tags" in data:
        import capo_clouddirectory.types.tag_list

        out["tags"] = capo_clouddirectory.types.tag_list.deserialize_json(data["Tags"])
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
