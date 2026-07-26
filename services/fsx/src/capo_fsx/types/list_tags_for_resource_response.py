"""Generated from Smithy shape ``com.amazonaws.fsx#ListTagsForResourceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fsx.types.next_token
    import capo_fsx.types.tags


class ListTagsForResourceResponse(TypedDict, closed=True):
    tags: NotRequired["capo_fsx.types.tags.Tags"]
    """<p>A list of tags on the resource.</p>"""
    next_token: NotRequired["capo_fsx.types.next_token.NextToken"]
    """<p>This is present if there are more tags than returned in the response (String). You can use the <code>NextToken</code> value in the later request to fetch the tags. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTagsForResourceResponse) -> dict:
    out: dict = {}
    if "tags" in value:
        import capo_fsx.types.tags

        out["Tags"] = capo_fsx.types.tags.serialize_aws_json_1_1(value["tags"])
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTagsForResourceResponse:
    out: ListTagsForResourceResponse = {}  # type: ignore[typeddict-item]
    if "Tags" in data:
        import capo_fsx.types.tags

        out["tags"] = capo_fsx.types.tags.deserialize_aws_json_1_1(data["Tags"])
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
