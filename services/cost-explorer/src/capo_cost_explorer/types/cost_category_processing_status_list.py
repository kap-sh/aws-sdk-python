"""Generated from Smithy shape ``com.amazonaws.costexplorer#CostCategoryProcessingStatusList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cost_explorer.types.cost_category_processing_status

CostCategoryProcessingStatusList: TypeAlias = list[
    "capo_cost_explorer.types.cost_category_processing_status.CostCategoryProcessingStatus"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CostCategoryProcessingStatusList) -> list:
    import capo_cost_explorer.types.cost_category_processing_status

    out: list = []
    for item in value:
        out.append(
            capo_cost_explorer.types.cost_category_processing_status.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> CostCategoryProcessingStatusList:
    import capo_cost_explorer.types.cost_category_processing_status

    out: CostCategoryProcessingStatusList = []
    for item in data:
        out.append(
            capo_cost_explorer.types.cost_category_processing_status.deserialize_aws_json_1_1(
                item
            )
        )
    return out
