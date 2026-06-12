"""Generated from Smithy shape ``com.amazonaws.connect#SearchResourceTagsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.next_token2500
    import aws_sdk_connect.types.tags_list


class SearchResourceTagsResponse(TypedDict):
    tags: NotRequired["aws_sdk_connect.types.tags_list.TagsList"]
    """<p>A list of tags used in the Connect Customer instance.</p>"""
    next_token: NotRequired["aws_sdk_connect.types.next_token2500.NextToken2500"]
    """<p>If there are additional results, this is the token for the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchResourceTagsResponse) -> dict:
    out: dict = {}
    if "tags" in value:
        import aws_sdk_connect.types.tags_list

        out["Tags"] = aws_sdk_connect.types.tags_list.serialize_json(value["tags"])
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> SearchResourceTagsResponse:
    out: SearchResourceTagsResponse = {}  # type: ignore[typeddict-item]
    if "Tags" in data:
        import aws_sdk_connect.types.tags_list

        out["tags"] = aws_sdk_connect.types.tags_list.deserialize_json(data["Tags"])
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
