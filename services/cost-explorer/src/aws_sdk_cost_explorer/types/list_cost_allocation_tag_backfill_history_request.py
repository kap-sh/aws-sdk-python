"""Generated from Smithy shape ``com.amazonaws.costexplorer#ListCostAllocationTagBackfillHistoryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.cost_allocation_tags_max_results
    import aws_sdk_cost_explorer.types.next_page_token


class ListCostAllocationTagBackfillHistoryRequest(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_cost_explorer.types.next_page_token.NextPageToken"]
    """<p> The token to retrieve the next set of results. Amazon Web Services provides the token when the response from a previous call has more results than the maximum page size. </p>"""
    max_results: NotRequired[
        "aws_sdk_cost_explorer.types.cost_allocation_tags_max_results.CostAllocationTagsMaxResults"
    ]
    """<p> The maximum number of objects that are returned for this request. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListCostAllocationTagBackfillHistoryRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListCostAllocationTagBackfillHistoryRequest:
    out: ListCostAllocationTagBackfillHistoryRequest = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
