"""Generated from Smithy shape ``com.amazonaws.costexplorer#DescribeCostCategoryDefinitionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cost_explorer.types.cost_category


class DescribeCostCategoryDefinitionResponse(TypedDict, closed=True):
    cost_category: NotRequired["capo_cost_explorer.types.cost_category.CostCategory"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeCostCategoryDefinitionResponse) -> dict:
    out: dict = {}
    if "cost_category" in value:
        import capo_cost_explorer.types.cost_category

        out["CostCategory"] = (
            capo_cost_explorer.types.cost_category.serialize_aws_json_1_1(
                value["cost_category"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeCostCategoryDefinitionResponse:
    out: DescribeCostCategoryDefinitionResponse = {}  # type: ignore[typeddict-item]
    if "CostCategory" in data:
        import capo_cost_explorer.types.cost_category

        out["cost_category"] = (
            capo_cost_explorer.types.cost_category.deserialize_aws_json_1_1(
                data["CostCategory"]
            )
        )
    return out
