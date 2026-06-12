"""Generated from Smithy shape ``com.amazonaws.costexplorer#CostCategoryNamesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.cost_category_name

CostCategoryNamesList: TypeAlias = list[
    "aws_sdk_cost_explorer.types.cost_category_name.CostCategoryName"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CostCategoryNamesList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> CostCategoryNamesList:
    return list(data)
