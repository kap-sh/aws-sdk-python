"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationFormSingleSelectQuestionAutomationOption``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_connect.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.single_select_question_rule_category_automation


class _EvaluationFormSingleSelectQuestionAutomationOption_RuleCategory(TypedDict):
    RuleCategory: "aws_sdk_connect.types.single_select_question_rule_category_automation.SingleSelectQuestionRuleCategoryAutomation"


EvaluationFormSingleSelectQuestionAutomationOption: TypeAlias = (
    _EvaluationFormSingleSelectQuestionAutomationOption_RuleCategory
)


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationFormSingleSelectQuestionAutomationOption) -> dict:
    if "RuleCategory" in value:
        import aws_sdk_connect.types.single_select_question_rule_category_automation

        return {
            "RuleCategory": aws_sdk_connect.types.single_select_question_rule_category_automation.serialize_json(
                value["RuleCategory"]
            )
        }
    else:
        raise SerializationError(
            "EvaluationFormSingleSelectQuestionAutomationOption: no variant present"
        )


def deserialize_json(data: dict) -> EvaluationFormSingleSelectQuestionAutomationOption:
    if "RuleCategory" in data:
        import aws_sdk_connect.types.single_select_question_rule_category_automation

        return {
            "RuleCategory": aws_sdk_connect.types.single_select_question_rule_category_automation.deserialize_json(
                data["RuleCategory"]
            )
        }
    else:
        raise DeserializationError(
            "EvaluationFormSingleSelectQuestionAutomationOption: no recognized variant key"
        )
