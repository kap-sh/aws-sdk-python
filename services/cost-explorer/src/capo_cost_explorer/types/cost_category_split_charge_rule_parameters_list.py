"""Generated from Smithy shape ``com.amazonaws.costexplorer#CostCategorySplitChargeRuleParametersList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cost_explorer.types.cost_category_split_charge_rule_parameter

CostCategorySplitChargeRuleParametersList: TypeAlias = list[
    "capo_cost_explorer.types.cost_category_split_charge_rule_parameter.CostCategorySplitChargeRuleParameter"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CostCategorySplitChargeRuleParametersList) -> list:
    import capo_cost_explorer.types.cost_category_split_charge_rule_parameter

    out: list = []
    for item in value:
        out.append(
            capo_cost_explorer.types.cost_category_split_charge_rule_parameter.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> CostCategorySplitChargeRuleParametersList:
    import capo_cost_explorer.types.cost_category_split_charge_rule_parameter

    out: CostCategorySplitChargeRuleParametersList = []
    for item in data:
        out.append(
            capo_cost_explorer.types.cost_category_split_charge_rule_parameter.deserialize_aws_json_1_1(
                item
            )
        )
    return out
