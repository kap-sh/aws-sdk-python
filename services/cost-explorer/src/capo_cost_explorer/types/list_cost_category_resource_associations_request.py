"""Generated from Smithy shape ``com.amazonaws.costexplorer#ListCostCategoryResourceAssociationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cost_explorer.types.arn
    import capo_cost_explorer.types.cost_category_max_results
    import capo_cost_explorer.types.next_page_token


class ListCostCategoryResourceAssociationsRequest(TypedDict, closed=True):
    cost_category_arn: NotRequired["capo_cost_explorer.types.arn.Arn"]
    """<p>The unique identifier for your cost category.</p>"""
    next_token: NotRequired["capo_cost_explorer.types.next_page_token.NextPageToken"]
    """<p> The token to retrieve the next set of results. Amazon Web Services provides the token when the response from a previous call has more results than the maximum page size. </p>"""
    max_results: NotRequired[
        "capo_cost_explorer.types.cost_category_max_results.CostCategoryMaxResults"
    ]
    """<p> The number of entries a paginated response contains. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListCostCategoryResourceAssociationsRequest) -> dict:
    out: dict = {}
    if "cost_category_arn" in value:
        out["CostCategoryArn"] = value["cost_category_arn"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListCostCategoryResourceAssociationsRequest:
    out: ListCostCategoryResourceAssociationsRequest = {}  # type: ignore[typeddict-item]
    if "CostCategoryArn" in data:
        out["cost_category_arn"] = data["CostCategoryArn"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
