"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationFormQuestion``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.boolean
    import aws_sdk_connect.types.evaluation_form_item_enablement_configuration
    import aws_sdk_connect.types.evaluation_form_item_weight
    import aws_sdk_connect.types.evaluation_form_question_instructions
    import aws_sdk_connect.types.evaluation_form_question_title
    import aws_sdk_connect.types.evaluation_form_question_type
    import aws_sdk_connect.types.evaluation_form_question_type_properties
    import aws_sdk_connect.types.reference_id


class EvaluationFormQuestion(TypedDict, closed=True):
    title: "aws_sdk_connect.types.evaluation_form_question_title.EvaluationFormQuestionTitle"
    """<p>The title of the question.</p>"""
    instructions: NotRequired[
        "aws_sdk_connect.types.evaluation_form_question_instructions.EvaluationFormQuestionInstructions"
    ]
    """<p>The instructions of the section.</p>"""
    ref_id: "aws_sdk_connect.types.reference_id.ReferenceId"
    """<p>The identifier of the question. An identifier must be unique within the evaluation form.</p>"""
    not_applicable_enabled: "aws_sdk_connect.types.boolean.Boolean"
    """<p>The flag to enable not applicable answers to the question.</p>"""
    question_type: (
        "aws_sdk_connect.types.evaluation_form_question_type.EvaluationFormQuestionType"
    )
    """<p>The type of the question.</p>"""
    question_type_properties: NotRequired[
        "aws_sdk_connect.types.evaluation_form_question_type_properties.EvaluationFormQuestionTypeProperties"
    ]
    """<p>The properties of the type of question. Text questions do not have to define question type properties.</p>"""
    enablement: NotRequired[
        "aws_sdk_connect.types.evaluation_form_item_enablement_configuration.EvaluationFormItemEnablementConfiguration"
    ]
    """<p>A question conditional enablement.</p>"""
    weight: "aws_sdk_connect.types.evaluation_form_item_weight.EvaluationFormItemWeight"
    """<p>The scoring weight of the section.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationFormQuestion) -> dict:
    out: dict = {}
    out["Title"] = value["title"]
    if "instructions" in value:
        out["Instructions"] = value["instructions"]
    out["RefId"] = value["ref_id"]
    out["NotApplicableEnabled"] = value.get("not_applicable_enabled", False)
    import aws_sdk_connect.types.evaluation_form_question_type

    out["QuestionType"] = (
        aws_sdk_connect.types.evaluation_form_question_type.serialize_json(
            value["question_type"]
        )
    )
    if "question_type_properties" in value:
        import aws_sdk_connect.types.evaluation_form_question_type_properties

        out["QuestionTypeProperties"] = (
            aws_sdk_connect.types.evaluation_form_question_type_properties.serialize_json(
                value["question_type_properties"]
            )
        )
    if "enablement" in value:
        import aws_sdk_connect.types.evaluation_form_item_enablement_configuration

        out["Enablement"] = (
            aws_sdk_connect.types.evaluation_form_item_enablement_configuration.serialize_json(
                value["enablement"]
            )
        )
    out["Weight"] = value.get("weight", 0)
    return out


def deserialize_json(data: dict) -> EvaluationFormQuestion:
    out: EvaluationFormQuestion = {}  # type: ignore[typeddict-item]
    if "Title" in data:
        out["title"] = data["Title"]
    else:
        raise DeserializationError("EvaluationFormQuestion.title required")
    if "Instructions" in data:
        out["instructions"] = data["Instructions"]
    if "RefId" in data:
        out["ref_id"] = data["RefId"]
    else:
        raise DeserializationError("EvaluationFormQuestion.ref_id required")
    if "NotApplicableEnabled" in data:
        out["not_applicable_enabled"] = data["NotApplicableEnabled"]
    else:
        out["not_applicable_enabled"] = False
    if "QuestionType" in data:
        import aws_sdk_connect.types.evaluation_form_question_type

        out["question_type"] = (
            aws_sdk_connect.types.evaluation_form_question_type.deserialize_json(
                data["QuestionType"]
            )
        )
    else:
        raise DeserializationError("EvaluationFormQuestion.question_type required")
    if "QuestionTypeProperties" in data:
        import aws_sdk_connect.types.evaluation_form_question_type_properties

        out["question_type_properties"] = (
            aws_sdk_connect.types.evaluation_form_question_type_properties.deserialize_json(
                data["QuestionTypeProperties"]
            )
        )
    if "Enablement" in data:
        import aws_sdk_connect.types.evaluation_form_item_enablement_configuration

        out["enablement"] = (
            aws_sdk_connect.types.evaluation_form_item_enablement_configuration.deserialize_json(
                data["Enablement"]
            )
        )
    if "Weight" in data:
        out["weight"] = data["Weight"]
    else:
        out["weight"] = 0
    return out
