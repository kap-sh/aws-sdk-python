"""Generated from Smithy shape ``com.amazonaws.costexplorer#CostCategoryResourceAssociations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.cost_category_resource_association

CostCategoryResourceAssociations: TypeAlias = list[
    "aws_sdk_cost_explorer.types.cost_category_resource_association.CostCategoryResourceAssociation"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CostCategoryResourceAssociations) -> list:
    import aws_sdk_cost_explorer.types.cost_category_resource_association

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cost_explorer.types.cost_category_resource_association.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> CostCategoryResourceAssociations:
    import aws_sdk_cost_explorer.types.cost_category_resource_association

    out: CostCategoryResourceAssociations = []
    for item in data:
        out.append(
            aws_sdk_cost_explorer.types.cost_category_resource_association.deserialize_aws_json_1_1(
                item
            )
        )
    return out
