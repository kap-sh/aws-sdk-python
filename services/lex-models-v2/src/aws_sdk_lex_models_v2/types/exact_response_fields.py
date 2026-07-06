"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#ExactResponseFields``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.answer_field
    import aws_sdk_lex_models_v2.types.question_field


class ExactResponseFields(TypedDict, closed=True):
    question_field: "aws_sdk_lex_models_v2.types.question_field.QuestionField"
    """<p>The name of the field that contains the query made to the OpenSearch Service database.</p>"""
    answer_field: "aws_sdk_lex_models_v2.types.answer_field.AnswerField"
    """<p>The name of the field that contains the answer to the query made to the OpenSearch Service database.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExactResponseFields) -> dict:
    out: dict = {}
    out["questionField"] = value["question_field"]
    out["answerField"] = value["answer_field"]
    return out


def deserialize_json(data: dict) -> ExactResponseFields:
    out: ExactResponseFields = {}  # type: ignore[typeddict-item]
    if "questionField" in data:
        out["question_field"] = data["questionField"]
    else:
        raise DeserializationError("ExactResponseFields.question_field required")
    if "answerField" in data:
        out["answer_field"] = data["answerField"]
    else:
        raise DeserializationError("ExactResponseFields.answer_field required")
    return out
