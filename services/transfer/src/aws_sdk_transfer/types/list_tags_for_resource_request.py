"""Generated from Smithy shape ``com.amazonaws.transfer#ListTagsForResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_transfer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_transfer.types.arn
    import aws_sdk_transfer.types.max_results
    import aws_sdk_transfer.types.next_token


class ListTagsForResourceRequest(TypedDict, closed=True):
    arn: "aws_sdk_transfer.types.arn.Arn"
    """<p>Requests the tags associated with a particular Amazon Resource Name (ARN). An ARN is an identifier for a specific Amazon Web Services resource, such as a server, user, or role.</p>"""
    max_results: NotRequired["aws_sdk_transfer.types.max_results.MaxResults"]
    """<p>Specifies the number of tags to return as a response to the <code>ListTagsForResource</code> request.</p>"""
    next_token: NotRequired["aws_sdk_transfer.types.next_token.NextToken"]
    """<p>When you request additional results from the <code>ListTagsForResource</code> operation, a <code>NextToken</code> parameter is returned in the input. You can then pass in a subsequent command to the <code>NextToken</code> parameter to continue listing additional tags.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTagsForResourceRequest) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTagsForResourceRequest:
    out: ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("ListTagsForResourceRequest.arn required")
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
