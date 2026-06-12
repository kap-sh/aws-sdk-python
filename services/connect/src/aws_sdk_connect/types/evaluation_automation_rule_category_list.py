"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationAutomationRuleCategoryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.evaluation_automation_rule_category

EvaluationAutomationRuleCategoryList: TypeAlias = list[
    "aws_sdk_connect.types.evaluation_automation_rule_category.EvaluationAutomationRuleCategory"
]


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationAutomationRuleCategoryList) -> list:
    import aws_sdk_connect.types.evaluation_automation_rule_category

    out: list = []
    for item in value:
        out.append(
            aws_sdk_connect.types.evaluation_automation_rule_category.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> EvaluationAutomationRuleCategoryList:
    import aws_sdk_connect.types.evaluation_automation_rule_category

    out: EvaluationAutomationRuleCategoryList = []
    for item in data:
        out.append(
            aws_sdk_connect.types.evaluation_automation_rule_category.deserialize_json(
                item
            )
        )
    return out
