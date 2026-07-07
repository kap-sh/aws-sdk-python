"""Generated from Smithy shape ``com.amazonaws.efs#ListTagsForResourceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_efs.types.tags
    import aws_sdk_efs.types.token


class ListTagsForResourceResponse(TypedDict, closed=True):
    tags: NotRequired["aws_sdk_efs.types.tags.Tags"]
    """<p>An array of the tags for the specified EFS resource.</p>"""
    next_token: NotRequired["aws_sdk_efs.types.token.Token"]
    """<p> <code>NextToken</code> is present if the response payload is paginated. You can use <code>NextToken</code> in a subsequent request to fetch the next page of access point descriptions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceResponse) -> dict:
    out: dict = {}
    if "tags" in value:
        import aws_sdk_efs.types.tags

        out["Tags"] = aws_sdk_efs.types.tags.serialize_json(value["tags"])
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListTagsForResourceResponse:
    out: ListTagsForResourceResponse = {}  # type: ignore[typeddict-item]
    if "Tags" in data:
        import aws_sdk_efs.types.tags

        out["tags"] = aws_sdk_efs.types.tags.deserialize_json(data["Tags"])
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
