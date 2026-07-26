"""Generated from Smithy shape ``com.amazonaws.costexplorer#CostCategorySplitChargeRuleTargetsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cost_explorer.types.generic_string

CostCategorySplitChargeRuleTargetsList: TypeAlias = list[
    "capo_cost_explorer.types.generic_string.GenericString"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CostCategorySplitChargeRuleTargetsList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> CostCategorySplitChargeRuleTargetsList:
    return list(data)
