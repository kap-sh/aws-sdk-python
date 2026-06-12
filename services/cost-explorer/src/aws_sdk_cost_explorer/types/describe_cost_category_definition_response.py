"""Generated from Smithy shape ``com.amazonaws.costexplorer#DescribeCostCategoryDefinitionResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.cost_category


class DescribeCostCategoryDefinitionResponse(TypedDict):
    cost_category: NotRequired["aws_sdk_cost_explorer.types.cost_category.CostCategory"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeCostCategoryDefinitionResponse) -> dict:
    out: dict = {}
    if "cost_category" in value:
        import aws_sdk_cost_explorer.types.cost_category

        out["CostCategory"] = (
            aws_sdk_cost_explorer.types.cost_category.serialize_aws_json_1_1(
                value["cost_category"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeCostCategoryDefinitionResponse:
    out: DescribeCostCategoryDefinitionResponse = {}  # type: ignore[typeddict-item]
    if "CostCategory" in data:
        import aws_sdk_cost_explorer.types.cost_category

        out["cost_category"] = (
            aws_sdk_cost_explorer.types.cost_category.deserialize_aws_json_1_1(
                data["CostCategory"]
            )
        )
    return out
