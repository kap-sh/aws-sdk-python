"""Generated from Smithy shape ``com.amazonaws.transfer#ListTagsForResourceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_transfer.types.arn
    import capo_transfer.types.next_token
    import capo_transfer.types.tags


class ListTagsForResourceResponse(TypedDict, closed=True):
    arn: NotRequired["capo_transfer.types.arn.Arn"]
    """<p>The ARN you specified to list the tags of.</p>"""
    next_token: NotRequired["capo_transfer.types.next_token.NextToken"]
    """<p>When you can get additional results from the <code>ListTagsForResource</code> call, a <code>NextToken</code> parameter is returned in the output. You can then pass in a subsequent command to the <code>NextToken</code> parameter to continue listing additional tags.</p>"""
    tags: NotRequired["capo_transfer.types.tags.Tags"]
    """<p>Key-value pairs that are assigned to a resource, usually for the purpose of grouping and searching for items. Tags are metadata that you define.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTagsForResourceResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "tags" in value:
        import capo_transfer.types.tags

        out["Tags"] = capo_transfer.types.tags.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTagsForResourceResponse:
    out: ListTagsForResourceResponse = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "Tags" in data:
        import capo_transfer.types.tags

        out["tags"] = capo_transfer.types.tags.deserialize_aws_json_1_1(data["Tags"])
    return out
