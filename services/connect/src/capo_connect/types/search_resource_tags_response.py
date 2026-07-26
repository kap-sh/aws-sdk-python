"""Generated from Smithy shape ``com.amazonaws.connect#SearchResourceTagsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.next_token2500
    import capo_connect.types.tags_list


class SearchResourceTagsResponse(TypedDict, closed=True):
    tags: NotRequired["capo_connect.types.tags_list.TagsList"]
    """<p>A list of tags used in the Connect Customer instance.</p>"""
    next_token: NotRequired["capo_connect.types.next_token2500.NextToken2500"]
    """<p>If there are additional results, this is the token for the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchResourceTagsResponse) -> dict:
    out: dict = {}
    if "tags" in value:
        import capo_connect.types.tags_list

        out["Tags"] = capo_connect.types.tags_list.serialize_json(value["tags"])
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> SearchResourceTagsResponse:
    out: SearchResourceTagsResponse = {}  # type: ignore[typeddict-item]
    if "Tags" in data:
        import capo_connect.types.tags_list

        out["tags"] = capo_connect.types.tags_list.deserialize_json(data["Tags"])
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
