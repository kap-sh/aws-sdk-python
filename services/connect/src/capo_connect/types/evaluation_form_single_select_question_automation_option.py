"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationFormSingleSelectQuestionAutomationOption``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_connect.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_connect.types.single_select_question_rule_category_automation


class _EvaluationFormSingleSelectQuestionAutomationOption_RuleCategory(
    TypedDict, closed=True
):
    RuleCategory: "capo_connect.types.single_select_question_rule_category_automation.SingleSelectQuestionRuleCategoryAutomation"


EvaluationFormSingleSelectQuestionAutomationOption: TypeAlias = (
    _EvaluationFormSingleSelectQuestionAutomationOption_RuleCategory
)


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationFormSingleSelectQuestionAutomationOption) -> dict:
    if "RuleCategory" in value:
        import capo_connect.types.single_select_question_rule_category_automation

        return {
            "RuleCategory": capo_connect.types.single_select_question_rule_category_automation.serialize_json(
                value["RuleCategory"]
            )
        }
    else:
        raise SerializationError(
            "EvaluationFormSingleSelectQuestionAutomationOption: no variant present"
        )


def deserialize_json(data: dict) -> EvaluationFormSingleSelectQuestionAutomationOption:
    if "RuleCategory" in data:
        import capo_connect.types.single_select_question_rule_category_automation

        return {
            "RuleCategory": capo_connect.types.single_select_question_rule_category_automation.deserialize_json(
                data["RuleCategory"]
            )
        }
    else:
        raise DeserializationError(
            "EvaluationFormSingleSelectQuestionAutomationOption: no recognized variant key"
        )
