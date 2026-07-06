"""Generated from Smithy shape ``com.amazonaws.costexplorer#ListCostAllocationTagsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.cost_allocation_tag_list
    import aws_sdk_cost_explorer.types.next_page_token


class ListCostAllocationTagsResponse(TypedDict, closed=True):
    cost_allocation_tags: NotRequired[
        "aws_sdk_cost_explorer.types.cost_allocation_tag_list.CostAllocationTagList"
    ]
    """<p>A list of cost allocation tags that includes the detailed metadata for each one. </p>"""
    next_token: NotRequired["aws_sdk_cost_explorer.types.next_page_token.NextPageToken"]
    """<p>The token to retrieve the next set of results. Amazon Web Services provides the token when the response from a previous call has more results than the maximum page size. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListCostAllocationTagsResponse) -> dict:
    out: dict = {}
    if "cost_allocation_tags" in value:
        import aws_sdk_cost_explorer.types.cost_allocation_tag_list

        out["CostAllocationTags"] = (
            aws_sdk_cost_explorer.types.cost_allocation_tag_list.serialize_aws_json_1_1(
                value["cost_allocation_tags"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListCostAllocationTagsResponse:
    out: ListCostAllocationTagsResponse = {}  # type: ignore[typeddict-item]
    if "CostAllocationTags" in data:
        import aws_sdk_cost_explorer.types.cost_allocation_tag_list

        out["cost_allocation_tags"] = (
            aws_sdk_cost_explorer.types.cost_allocation_tag_list.deserialize_aws_json_1_1(
                data["CostAllocationTags"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
