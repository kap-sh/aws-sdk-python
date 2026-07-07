"""Generated from Smithy shape ``com.amazonaws.ssm#DescribeInventoryDeletionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ssm.types.max_results
    import aws_sdk_ssm.types.next_token
    import aws_sdk_ssm.types.uuid


class DescribeInventoryDeletionsRequest(TypedDict, closed=True):
    deletion_id: NotRequired["aws_sdk_ssm.types.uuid.UUID"]
    """<p>Specify the delete inventory ID for which you want information. This ID was returned by the <code>DeleteInventory</code> operation.</p>"""
    next_token: NotRequired["aws_sdk_ssm.types.next_token.NextToken"]
    """<p>A token to start the list. Use this token to get the next set of results. </p>"""
    max_results: NotRequired["aws_sdk_ssm.types.max_results.MaxResults"]
    """<p>The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeInventoryDeletionsRequest) -> dict:
    out: dict = {}
    if "deletion_id" in value:
        out["DeletionId"] = value["deletion_id"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeInventoryDeletionsRequest:
    out: DescribeInventoryDeletionsRequest = {}  # type: ignore[typeddict-item]
    if "DeletionId" in data:
        out["deletion_id"] = data["DeletionId"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
