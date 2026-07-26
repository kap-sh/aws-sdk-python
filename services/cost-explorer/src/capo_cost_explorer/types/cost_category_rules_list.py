"""Generated from Smithy shape ``com.amazonaws.costexplorer#CostCategoryRulesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cost_explorer.types.cost_category_rule

CostCategoryRulesList: TypeAlias = list[
    "capo_cost_explorer.types.cost_category_rule.CostCategoryRule"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CostCategoryRulesList) -> list:
    import capo_cost_explorer.types.cost_category_rule

    out: list = []
    for item in value:
        out.append(
            capo_cost_explorer.types.cost_category_rule.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> CostCategoryRulesList:
    import capo_cost_explorer.types.cost_category_rule

    out: CostCategoryRulesList = []
    for item in data:
        out.append(
            capo_cost_explorer.types.cost_category_rule.deserialize_aws_json_1_1(item)
        )
    return out
