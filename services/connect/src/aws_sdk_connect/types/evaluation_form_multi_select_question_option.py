"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationFormMultiSelectQuestionOption``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.evaluation_form_multi_select_question_option_text
    import aws_sdk_connect.types.reference_id


class EvaluationFormMultiSelectQuestionOption(TypedDict, closed=True):
    ref_id: "aws_sdk_connect.types.reference_id.ReferenceId"
    """<p>Reference identifier for this option.</p>"""
    text: "aws_sdk_connect.types.evaluation_form_multi_select_question_option_text.EvaluationFormMultiSelectQuestionOptionText"
    """<p>Display text for this option.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationFormMultiSelectQuestionOption) -> dict:
    out: dict = {}
    out["RefId"] = value["ref_id"]
    out["Text"] = value["text"]
    return out


def deserialize_json(data: dict) -> EvaluationFormMultiSelectQuestionOption:
    out: EvaluationFormMultiSelectQuestionOption = {}  # type: ignore[typeddict-item]
    if "RefId" in data:
        out["ref_id"] = data["RefId"]
    else:
        raise DeserializationError(
            "EvaluationFormMultiSelectQuestionOption.ref_id required"
        )
    if "Text" in data:
        out["text"] = data["Text"]
    else:
        raise DeserializationError(
            "EvaluationFormMultiSelectQuestionOption.text required"
        )
    return out
