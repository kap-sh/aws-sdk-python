"""Generated from Smithy shape ``com.amazonaws.costexplorer#CostCategorySplitChargeRulesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.cost_category_split_charge_rule

CostCategorySplitChargeRulesList: TypeAlias = list[
    "aws_sdk_cost_explorer.types.cost_category_split_charge_rule.CostCategorySplitChargeRule"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CostCategorySplitChargeRulesList) -> list:
    import aws_sdk_cost_explorer.types.cost_category_split_charge_rule

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cost_explorer.types.cost_category_split_charge_rule.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> CostCategorySplitChargeRulesList:
    import aws_sdk_cost_explorer.types.cost_category_split_charge_rule

    out: CostCategorySplitChargeRulesList = []
    for item in data:
        out.append(
            aws_sdk_cost_explorer.types.cost_category_split_charge_rule.deserialize_aws_json_1_1(
                item
            )
        )
    return out
