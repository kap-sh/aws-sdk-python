"""Generated from Smithy shape ``com.amazonaws.iotthingsgraph#ListTagsForResourceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotthingsgraph.types.next_token
    import capo_iotthingsgraph.types.tag_list


class ListTagsForResourceResponse(TypedDict, closed=True):
    tags: NotRequired["capo_iotthingsgraph.types.tag_list.TagList"]
    """<p>List of tags returned by the <code>ListTagsForResource</code> operation.</p>"""
    next_token: NotRequired["capo_iotthingsgraph.types.next_token.NextToken"]
    """<p>The token that specifies the next page of results to return.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTagsForResourceResponse) -> dict:
    out: dict = {}
    if "tags" in value:
        import capo_iotthingsgraph.types.tag_list

        out["tags"] = capo_iotthingsgraph.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTagsForResourceResponse:
    out: ListTagsForResourceResponse = {}  # type: ignore[typeddict-item]
    if "tags" in data:
        import capo_iotthingsgraph.types.tag_list

        out["tags"] = capo_iotthingsgraph.types.tag_list.deserialize_aws_json_1_1(
            data["tags"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
