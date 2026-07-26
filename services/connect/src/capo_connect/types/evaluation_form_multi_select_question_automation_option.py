"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationFormMultiSelectQuestionAutomationOption``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_connect.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_connect.types.multi_select_question_rule_category_automation


class _EvaluationFormMultiSelectQuestionAutomationOption_RuleCategory(
    TypedDict, closed=True
):
    RuleCategory: "capo_connect.types.multi_select_question_rule_category_automation.MultiSelectQuestionRuleCategoryAutomation"


EvaluationFormMultiSelectQuestionAutomationOption: TypeAlias = (
    _EvaluationFormMultiSelectQuestionAutomationOption_RuleCategory
)


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationFormMultiSelectQuestionAutomationOption) -> dict:
    if "RuleCategory" in value:
        import capo_connect.types.multi_select_question_rule_category_automation

        return {
            "RuleCategory": capo_connect.types.multi_select_question_rule_category_automation.serialize_json(
                value["RuleCategory"]
            )
        }
    else:
        raise SerializationError(
            "EvaluationFormMultiSelectQuestionAutomationOption: no variant present"
        )


def deserialize_json(data: dict) -> EvaluationFormMultiSelectQuestionAutomationOption:
    if "RuleCategory" in data:
        import capo_connect.types.multi_select_question_rule_category_automation

        return {
            "RuleCategory": capo_connect.types.multi_select_question_rule_category_automation.deserialize_json(
                data["RuleCategory"]
            )
        }
    else:
        raise DeserializationError(
            "EvaluationFormMultiSelectQuestionAutomationOption: no recognized variant key"
        )
