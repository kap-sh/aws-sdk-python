"""Generated from Smithy shape ``com.amazonaws.costexplorer#CostCategorySplitChargeRuleParameterValuesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cost_explorer.types.generic_string

CostCategorySplitChargeRuleParameterValuesList: TypeAlias = list[
    "capo_cost_explorer.types.generic_string.GenericString"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: CostCategorySplitChargeRuleParameterValuesList,
) -> list:
    return list(value)


def deserialize_aws_json_1_1(
    data: list,
) -> CostCategorySplitChargeRuleParameterValuesList:
    return list(data)
