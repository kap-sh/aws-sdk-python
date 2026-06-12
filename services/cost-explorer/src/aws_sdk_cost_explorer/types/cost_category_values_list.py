"""Generated from Smithy shape ``com.amazonaws.costexplorer#CostCategoryValuesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.cost_category_value

CostCategoryValuesList: TypeAlias = list[
    "aws_sdk_cost_explorer.types.cost_category_value.CostCategoryValue"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CostCategoryValuesList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> CostCategoryValuesList:
    return list(data)
