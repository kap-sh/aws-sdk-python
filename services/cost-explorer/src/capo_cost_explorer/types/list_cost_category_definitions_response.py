"""Generated from Smithy shape ``com.amazonaws.costexplorer#ListCostCategoryDefinitionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cost_explorer.types.cost_category_references_list
    import capo_cost_explorer.types.next_page_token


class ListCostCategoryDefinitionsResponse(TypedDict, closed=True):
    cost_category_references: NotRequired[
        "capo_cost_explorer.types.cost_category_references_list.CostCategoryReferencesList"
    ]
    """<p>A reference to a cost category that contains enough information to identify the Cost Category. </p>"""
    next_token: NotRequired["capo_cost_explorer.types.next_page_token.NextPageToken"]
    """<p>The token to retrieve the next set of results. Amazon Web Services provides the token when the response from a previous call has more results than the maximum page size. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListCostCategoryDefinitionsResponse) -> dict:
    out: dict = {}
    if "cost_category_references" in value:
        import capo_cost_explorer.types.cost_category_references_list

        out["CostCategoryReferences"] = (
            capo_cost_explorer.types.cost_category_references_list.serialize_aws_json_1_1(
                value["cost_category_references"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListCostCategoryDefinitionsResponse:
    out: ListCostCategoryDefinitionsResponse = {}  # type: ignore[typeddict-item]
    if "CostCategoryReferences" in data:
        import capo_cost_explorer.types.cost_category_references_list

        out["cost_category_references"] = (
            capo_cost_explorer.types.cost_category_references_list.deserialize_aws_json_1_1(
                data["CostCategoryReferences"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
