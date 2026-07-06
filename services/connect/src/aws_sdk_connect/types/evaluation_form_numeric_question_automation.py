"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationFormNumericQuestionAutomation``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_connect.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.evaluation_form_question_automation_answer_source
    import aws_sdk_connect.types.numeric_question_property_value_automation


class _EvaluationFormNumericQuestionAutomation_PropertyValue(TypedDict, closed=True):
    PropertyValue: "aws_sdk_connect.types.numeric_question_property_value_automation.NumericQuestionPropertyValueAutomation"


class _EvaluationFormNumericQuestionAutomation_AnswerSource(TypedDict, closed=True):
    AnswerSource: "aws_sdk_connect.types.evaluation_form_question_automation_answer_source.EvaluationFormQuestionAutomationAnswerSource"


EvaluationFormNumericQuestionAutomation: TypeAlias = (
    _EvaluationFormNumericQuestionAutomation_PropertyValue
    | _EvaluationFormNumericQuestionAutomation_AnswerSource
)


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationFormNumericQuestionAutomation) -> dict:
    if "PropertyValue" in value:
        import aws_sdk_connect.types.numeric_question_property_value_automation

        return {
            "PropertyValue": aws_sdk_connect.types.numeric_question_property_value_automation.serialize_json(
                value["PropertyValue"]
            )
        }
    elif "AnswerSource" in value:
        import aws_sdk_connect.types.evaluation_form_question_automation_answer_source

        return {
            "AnswerSource": aws_sdk_connect.types.evaluation_form_question_automation_answer_source.serialize_json(
                value["AnswerSource"]
            )
        }
    else:
        raise SerializationError(
            "EvaluationFormNumericQuestionAutomation: no variant present"
        )


def deserialize_json(data: dict) -> EvaluationFormNumericQuestionAutomation:
    if "PropertyValue" in data:
        import aws_sdk_connect.types.numeric_question_property_value_automation

        return {
            "PropertyValue": aws_sdk_connect.types.numeric_question_property_value_automation.deserialize_json(
                data["PropertyValue"]
            )
        }
    elif "AnswerSource" in data:
        import aws_sdk_connect.types.evaluation_form_question_automation_answer_source

        return {
            "AnswerSource": aws_sdk_connect.types.evaluation_form_question_automation_answer_source.deserialize_json(
                data["AnswerSource"]
            )
        }
    else:
        raise DeserializationError(
            "EvaluationFormNumericQuestionAutomation: no recognized variant key"
        )
