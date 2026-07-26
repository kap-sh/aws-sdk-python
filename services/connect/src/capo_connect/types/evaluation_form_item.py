"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationFormItem``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_connect.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_connect.types.evaluation_form_question
    import capo_connect.types.evaluation_form_section


class _EvaluationFormItem_Section(TypedDict, closed=True):
    Section: "capo_connect.types.evaluation_form_section.EvaluationFormSection"


class _EvaluationFormItem_Question(TypedDict, closed=True):
    Question: "capo_connect.types.evaluation_form_question.EvaluationFormQuestion"


EvaluationFormItem: TypeAlias = (
    _EvaluationFormItem_Section | _EvaluationFormItem_Question
)


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationFormItem) -> dict:
    if "Section" in value:
        import capo_connect.types.evaluation_form_section

        return {
            "Section": capo_connect.types.evaluation_form_section.serialize_json(
                value["Section"]
            )
        }
    elif "Question" in value:
        import capo_connect.types.evaluation_form_question

        return {
            "Question": capo_connect.types.evaluation_form_question.serialize_json(
                value["Question"]
            )
        }
    else:
        raise SerializationError("EvaluationFormItem: no variant present")


def deserialize_json(data: dict) -> EvaluationFormItem:
    if "Section" in data:
        import capo_connect.types.evaluation_form_section

        return {
            "Section": capo_connect.types.evaluation_form_section.deserialize_json(
                data["Section"]
            )
        }
    elif "Question" in data:
        import capo_connect.types.evaluation_form_question

        return {
            "Question": capo_connect.types.evaluation_form_question.deserialize_json(
                data["Question"]
            )
        }
    else:
        raise DeserializationError("EvaluationFormItem: no recognized variant key")
