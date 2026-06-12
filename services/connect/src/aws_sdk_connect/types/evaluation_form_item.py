"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationFormItem``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_connect.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.evaluation_form_question
    import aws_sdk_connect.types.evaluation_form_section


class _EvaluationFormItem_Section(TypedDict):
    Section: "aws_sdk_connect.types.evaluation_form_section.EvaluationFormSection"


class _EvaluationFormItem_Question(TypedDict):
    Question: "aws_sdk_connect.types.evaluation_form_question.EvaluationFormQuestion"


EvaluationFormItem: TypeAlias = (
    _EvaluationFormItem_Section | _EvaluationFormItem_Question
)


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationFormItem) -> dict:
    if "Section" in value:
        import aws_sdk_connect.types.evaluation_form_section

        return {
            "Section": aws_sdk_connect.types.evaluation_form_section.serialize_json(
                value["Section"]
            )
        }
    elif "Question" in value:
        import aws_sdk_connect.types.evaluation_form_question

        return {
            "Question": aws_sdk_connect.types.evaluation_form_question.serialize_json(
                value["Question"]
            )
        }
    else:
        raise SerializationError("EvaluationFormItem: no variant present")


def deserialize_json(data: dict) -> EvaluationFormItem:
    if "Section" in data:
        import aws_sdk_connect.types.evaluation_form_section

        return {
            "Section": aws_sdk_connect.types.evaluation_form_section.deserialize_json(
                data["Section"]
            )
        }
    elif "Question" in data:
        import aws_sdk_connect.types.evaluation_form_question

        return {
            "Question": aws_sdk_connect.types.evaluation_form_question.deserialize_json(
                data["Question"]
            )
        }
    else:
        raise DeserializationError("EvaluationFormItem: no recognized variant key")
