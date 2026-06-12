"""Generated from Smithy shape ``com.amazonaws.costexplorer#ListCostCategoryResourceAssociationsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.cost_category_resource_associations
    import aws_sdk_cost_explorer.types.next_page_token


class ListCostCategoryResourceAssociationsResponse(TypedDict):
    cost_category_resource_associations: NotRequired[
        "aws_sdk_cost_explorer.types.cost_category_resource_associations.CostCategoryResourceAssociations"
    ]
    """<p> A reference to a cost category association that contains information on an associated resource. </p>"""
    next_token: NotRequired["aws_sdk_cost_explorer.types.next_page_token.NextPageToken"]
    """<p> The token to retrieve the next set of results. Amazon Web Services provides the token when the response from a previous call has more results than the maximum page size. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListCostCategoryResourceAssociationsResponse) -> dict:
    out: dict = {}
    if "cost_category_resource_associations" in value:
        import aws_sdk_cost_explorer.types.cost_category_resource_associations

        out["CostCategoryResourceAssociations"] = (
            aws_sdk_cost_explorer.types.cost_category_resource_associations.serialize_aws_json_1_1(
                value["cost_category_resource_associations"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> ListCostCategoryResourceAssociationsResponse:
    out: ListCostCategoryResourceAssociationsResponse = {}  # type: ignore[typeddict-item]
    if "CostCategoryResourceAssociations" in data:
        import aws_sdk_cost_explorer.types.cost_category_resource_associations

        out["cost_category_resource_associations"] = (
            aws_sdk_cost_explorer.types.cost_category_resource_associations.deserialize_aws_json_1_1(
                data["CostCategoryResourceAssociations"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
