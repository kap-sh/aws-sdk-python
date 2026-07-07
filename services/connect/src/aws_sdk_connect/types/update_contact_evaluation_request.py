"""Generated from Smithy shape ``com.amazonaws.connect#UpdateContactEvaluationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.evaluation_answers_input_map
    import aws_sdk_connect.types.evaluation_notes_map
    import aws_sdk_connect.types.evaluator_user_union
    import aws_sdk_connect.types.instance_id
    import aws_sdk_connect.types.resource_id


class UpdateContactEvaluationRequest(TypedDict, closed=True):
    instance_id: "aws_sdk_connect.types.instance_id.InstanceId"
    r"""<p>The identifier of the Connect Customer instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    evaluation_id: "aws_sdk_connect.types.resource_id.ResourceId"
    """<p>A unique identifier for the contact evaluation.</p>"""
    answers: NotRequired[
        "aws_sdk_connect.types.evaluation_answers_input_map.EvaluationAnswersInputMap"
    ]
    """<p>A map of question identifiers to answer value.</p>"""
    notes: NotRequired["aws_sdk_connect.types.evaluation_notes_map.EvaluationNotesMap"]
    """<p>A map of question identifiers to note value.</p>"""
    updated_by: NotRequired[
        "aws_sdk_connect.types.evaluator_user_union.EvaluatorUserUnion"
    ]
    """<p>The ID of the user who updated the contact evaluation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateContactEvaluationRequest) -> dict:
    out: dict = {}
    if "answers" in value:
        import aws_sdk_connect.types.evaluation_answers_input_map

        out["Answers"] = (
            aws_sdk_connect.types.evaluation_answers_input_map.serialize_json(
                value["answers"]
            )
        )
    if "notes" in value:
        import aws_sdk_connect.types.evaluation_notes_map

        out["Notes"] = aws_sdk_connect.types.evaluation_notes_map.serialize_json(
            value["notes"]
        )
    if "updated_by" in value:
        import aws_sdk_connect.types.evaluator_user_union

        out["UpdatedBy"] = aws_sdk_connect.types.evaluator_user_union.serialize_json(
            value["updated_by"]
        )
    return out


def deserialize_json(data: dict) -> UpdateContactEvaluationRequest:
    out: UpdateContactEvaluationRequest = {}  # type: ignore[typeddict-item]
    if "Answers" in data:
        import aws_sdk_connect.types.evaluation_answers_input_map

        out["answers"] = (
            aws_sdk_connect.types.evaluation_answers_input_map.deserialize_json(
                data["Answers"]
            )
        )
    if "Notes" in data:
        import aws_sdk_connect.types.evaluation_notes_map

        out["notes"] = aws_sdk_connect.types.evaluation_notes_map.deserialize_json(
            data["Notes"]
        )
    if "UpdatedBy" in data:
        import aws_sdk_connect.types.evaluator_user_union

        out["updated_by"] = aws_sdk_connect.types.evaluator_user_union.deserialize_json(
            data["UpdatedBy"]
        )
    return out
