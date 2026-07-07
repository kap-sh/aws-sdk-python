"""Generated from Smithy shape ``com.amazonaws.keyspaces#ListTagsForResourceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_keyspaces.types.next_token
    import aws_sdk_keyspaces.types.tag_list


class ListTagsForResourceResponse(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_keyspaces.types.next_token.NextToken"]
    """<p>A token to specify where to start paginating. This is the <code>NextToken</code> from a previously truncated response.</p>"""
    tags: NotRequired["aws_sdk_keyspaces.types.tag_list.TagList"]
    """<p>A list of tags.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListTagsForResourceResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "tags" in value:
        import aws_sdk_keyspaces.types.tag_list

        out["tags"] = aws_sdk_keyspaces.types.tag_list.serialize_aws_json_1_0(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListTagsForResourceResponse:
    out: ListTagsForResourceResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "tags" in data:
        import aws_sdk_keyspaces.types.tag_list

        out["tags"] = aws_sdk_keyspaces.types.tag_list.deserialize_aws_json_1_0(
            data["tags"]
        )
    return out
