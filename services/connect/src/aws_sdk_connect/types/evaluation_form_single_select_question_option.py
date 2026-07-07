"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationFormSingleSelectQuestionOption``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.automatic_fail_configuration
    import aws_sdk_connect.types.boolean
    import aws_sdk_connect.types.evaluation_form_question_answer_score
    import aws_sdk_connect.types.evaluation_form_single_select_question_option_text
    import aws_sdk_connect.types.reference_id


class EvaluationFormSingleSelectQuestionOption(TypedDict, closed=True):
    ref_id: "aws_sdk_connect.types.reference_id.ReferenceId"
    """<p>The identifier of the answer option. An identifier must be unique within the question.</p>"""
    text: "aws_sdk_connect.types.evaluation_form_single_select_question_option_text.EvaluationFormSingleSelectQuestionOptionText"
    """<p>The title of the answer option.</p>"""
    score: "aws_sdk_connect.types.evaluation_form_question_answer_score.EvaluationFormQuestionAnswerScore"
    """<p>The score assigned to the answer option.</p>"""
    automatic_fail: "aws_sdk_connect.types.boolean.Boolean"
    """<p>The flag to mark the option as automatic fail. If an automatic fail answer is provided, the overall evaluation gets a score of 0.</p>"""
    automatic_fail_configuration: NotRequired[
        "aws_sdk_connect.types.automatic_fail_configuration.AutomaticFailConfiguration"
    ]
    """<p>Whether automatic fail is configured on a single select question. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationFormSingleSelectQuestionOption) -> dict:
    out: dict = {}
    out["RefId"] = value["ref_id"]
    out["Text"] = value["text"]
    out["Score"] = value.get("score", 0)
    out["AutomaticFail"] = value.get("automatic_fail", False)
    if "automatic_fail_configuration" in value:
        import aws_sdk_connect.types.automatic_fail_configuration

        out["AutomaticFailConfiguration"] = (
            aws_sdk_connect.types.automatic_fail_configuration.serialize_json(
                value["automatic_fail_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> EvaluationFormSingleSelectQuestionOption:
    out: EvaluationFormSingleSelectQuestionOption = {}  # type: ignore[typeddict-item]
    if "RefId" in data:
        out["ref_id"] = data["RefId"]
    else:
        raise DeserializationError(
            "EvaluationFormSingleSelectQuestionOption.ref_id required"
        )
    if "Text" in data:
        out["text"] = data["Text"]
    else:
        raise DeserializationError(
            "EvaluationFormSingleSelectQuestionOption.text required"
        )
    if "Score" in data:
        out["score"] = data["Score"]
    else:
        out["score"] = 0
    if "AutomaticFail" in data:
        out["automatic_fail"] = data["AutomaticFail"]
    else:
        out["automatic_fail"] = False
    if "AutomaticFailConfiguration" in data:
        import aws_sdk_connect.types.automatic_fail_configuration

        out["automatic_fail_configuration"] = (
            aws_sdk_connect.types.automatic_fail_configuration.deserialize_json(
                data["AutomaticFailConfiguration"]
            )
        )
    return out
