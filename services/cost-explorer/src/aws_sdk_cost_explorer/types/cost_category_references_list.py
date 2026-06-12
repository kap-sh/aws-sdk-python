"""Generated from Smithy shape ``com.amazonaws.costexplorer#CostCategoryReferencesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.cost_category_reference

CostCategoryReferencesList: TypeAlias = list[
    "aws_sdk_cost_explorer.types.cost_category_reference.CostCategoryReference"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CostCategoryReferencesList) -> list:
    import aws_sdk_cost_explorer.types.cost_category_reference

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cost_explorer.types.cost_category_reference.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> CostCategoryReferencesList:
    import aws_sdk_cost_explorer.types.cost_category_reference

    out: CostCategoryReferencesList = []
    for item in data:
        out.append(
            aws_sdk_cost_explorer.types.cost_category_reference.deserialize_aws_json_1_1(
                item
            )
        )
    return out
