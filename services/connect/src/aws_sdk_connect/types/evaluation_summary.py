"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.arn
    import aws_sdk_connect.types.auto_evaluation_status
    import aws_sdk_connect.types.boolean
    import aws_sdk_connect.types.evaluation_acknowledgement_summary
    import aws_sdk_connect.types.evaluation_contact_participant
    import aws_sdk_connect.types.evaluation_form_title
    import aws_sdk_connect.types.evaluation_score
    import aws_sdk_connect.types.evaluation_status
    import aws_sdk_connect.types.evaluation_type
    import aws_sdk_connect.types.resource_id
    import aws_sdk_connect.types.timestamp


class EvaluationSummary(TypedDict):
    evaluation_id: "aws_sdk_connect.types.resource_id.ResourceId"
    """<p>A unique identifier for the contact evaluation.</p>"""
    evaluation_arn: "aws_sdk_connect.types.arn.ARN"
    """<p>The Amazon Resource Name (ARN) for the contact evaluation resource.</p>"""
    evaluation_form_title: (
        "aws_sdk_connect.types.evaluation_form_title.EvaluationFormTitle"
    )
    """<p>A title of the evaluation form.</p>"""
    evaluation_form_id: "aws_sdk_connect.types.resource_id.ResourceId"
    """<p>The unique identifier for the evaluation form.</p>"""
    calibration_session_id: NotRequired["aws_sdk_connect.types.resource_id.ResourceId"]
    """<p>The calibration session ID that this evaluation belongs to.</p>"""
    status: "aws_sdk_connect.types.evaluation_status.EvaluationStatus"
    """<p>The status of the contact evaluation.</p>"""
    auto_evaluation_enabled: "aws_sdk_connect.types.boolean.Boolean"
    """<p>Whether automated evaluation is enabled.</p>"""
    auto_evaluation_status: NotRequired[
        "aws_sdk_connect.types.auto_evaluation_status.AutoEvaluationStatus"
    ]
    """<p>The status of the contact auto evaluation. </p>"""
    evaluator_arn: "aws_sdk_connect.types.arn.ARN"
    """<p>The Amazon Resource Name (ARN) of the user who last updated the evaluation.</p>"""
    score: NotRequired["aws_sdk_connect.types.evaluation_score.EvaluationScore"]
    """<p>The overall score of the contact evaluation.</p>"""
    acknowledgement: NotRequired[
        "aws_sdk_connect.types.evaluation_acknowledgement_summary.EvaluationAcknowledgementSummary"
    ]
    """<p>Information related to evaluation acknowledgement.</p>"""
    evaluation_type: NotRequired["aws_sdk_connect.types.evaluation_type.EvaluationType"]
    """<p>Type of the evaluation. </p>"""
    created_time: "aws_sdk_connect.types.timestamp.Timestamp"
    """<p>The timestamp for when the evaluation was created.</p>"""
    last_modified_time: "aws_sdk_connect.types.timestamp.Timestamp"
    """<p>The timestamp for when the evaluation was last updated.</p>"""
    contact_participant: NotRequired[
        "aws_sdk_connect.types.evaluation_contact_participant.EvaluationContactParticipant"
    ]
    """<p>Information about a contact participant in the evaluation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationSummary) -> dict:
    out: dict = {}
    out["EvaluationId"] = value["evaluation_id"]
    out["EvaluationArn"] = value["evaluation_arn"]
    out["EvaluationFormTitle"] = value["evaluation_form_title"]
    out["EvaluationFormId"] = value["evaluation_form_id"]
    if "calibration_session_id" in value:
        out["CalibrationSessionId"] = value["calibration_session_id"]
    import aws_sdk_connect.types.evaluation_status

    out["Status"] = aws_sdk_connect.types.evaluation_status.serialize_json(
        value["status"]
    )
    out["AutoEvaluationEnabled"] = value.get("auto_evaluation_enabled", False)
    if "auto_evaluation_status" in value:
        import aws_sdk_connect.types.auto_evaluation_status

        out["AutoEvaluationStatus"] = (
            aws_sdk_connect.types.auto_evaluation_status.serialize_json(
                value["auto_evaluation_status"]
            )
        )
    out["EvaluatorArn"] = value["evaluator_arn"]
    if "score" in value:
        import aws_sdk_connect.types.evaluation_score

        out["Score"] = aws_sdk_connect.types.evaluation_score.serialize_json(
            value["score"]
        )
    if "acknowledgement" in value:
        import aws_sdk_connect.types.evaluation_acknowledgement_summary

        out["Acknowledgement"] = (
            aws_sdk_connect.types.evaluation_acknowledgement_summary.serialize_json(
                value["acknowledgement"]
            )
        )
    if "evaluation_type" in value:
        import aws_sdk_connect.types.evaluation_type

        out["EvaluationType"] = aws_sdk_connect.types.evaluation_type.serialize_json(
            value["evaluation_type"]
        )
    import aws_sdk_connect.types.timestamp

    out["CreatedTime"] = aws_sdk_connect.types.timestamp.serialize_json(
        value["created_time"]
    )
    import aws_sdk_connect.types.timestamp

    out["LastModifiedTime"] = aws_sdk_connect.types.timestamp.serialize_json(
        value["last_modified_time"]
    )
    if "contact_participant" in value:
        import aws_sdk_connect.types.evaluation_contact_participant

        out["ContactParticipant"] = (
            aws_sdk_connect.types.evaluation_contact_participant.serialize_json(
                value["contact_participant"]
            )
        )
    return out


def deserialize_json(data: dict) -> EvaluationSummary:
    out: EvaluationSummary = {}  # type: ignore[typeddict-item]
    if "EvaluationId" in data:
        out["evaluation_id"] = data["EvaluationId"]
    else:
        raise DeserializationError("EvaluationSummary.evaluation_id required")
    if "EvaluationArn" in data:
        out["evaluation_arn"] = data["EvaluationArn"]
    else:
        raise DeserializationError("EvaluationSummary.evaluation_arn required")
    if "EvaluationFormTitle" in data:
        out["evaluation_form_title"] = data["EvaluationFormTitle"]
    else:
        raise DeserializationError("EvaluationSummary.evaluation_form_title required")
    if "EvaluationFormId" in data:
        out["evaluation_form_id"] = data["EvaluationFormId"]
    else:
        raise DeserializationError("EvaluationSummary.evaluation_form_id required")
    if "CalibrationSessionId" in data:
        out["calibration_session_id"] = data["CalibrationSessionId"]
    if "Status" in data:
        import aws_sdk_connect.types.evaluation_status

        out["status"] = aws_sdk_connect.types.evaluation_status.deserialize_json(
            data["Status"]
        )
    else:
        raise DeserializationError("EvaluationSummary.status required")
    if "AutoEvaluationEnabled" in data:
        out["auto_evaluation_enabled"] = data["AutoEvaluationEnabled"]
    else:
        out["auto_evaluation_enabled"] = False
    if "AutoEvaluationStatus" in data:
        import aws_sdk_connect.types.auto_evaluation_status

        out["auto_evaluation_status"] = (
            aws_sdk_connect.types.auto_evaluation_status.deserialize_json(
                data["AutoEvaluationStatus"]
            )
        )
    if "EvaluatorArn" in data:
        out["evaluator_arn"] = data["EvaluatorArn"]
    else:
        raise DeserializationError("EvaluationSummary.evaluator_arn required")
    if "Score" in data:
        import aws_sdk_connect.types.evaluation_score

        out["score"] = aws_sdk_connect.types.evaluation_score.deserialize_json(
            data["Score"]
        )
    if "Acknowledgement" in data:
        import aws_sdk_connect.types.evaluation_acknowledgement_summary

        out["acknowledgement"] = (
            aws_sdk_connect.types.evaluation_acknowledgement_summary.deserialize_json(
                data["Acknowledgement"]
            )
        )
    if "EvaluationType" in data:
        import aws_sdk_connect.types.evaluation_type

        out["evaluation_type"] = aws_sdk_connect.types.evaluation_type.deserialize_json(
            data["EvaluationType"]
        )
    if "CreatedTime" in data:
        import aws_sdk_connect.types.timestamp

        out["created_time"] = aws_sdk_connect.types.timestamp.deserialize_json(
            data["CreatedTime"]
        )
    else:
        raise DeserializationError("EvaluationSummary.created_time required")
    if "LastModifiedTime" in data:
        import aws_sdk_connect.types.timestamp

        out["last_modified_time"] = aws_sdk_connect.types.timestamp.deserialize_json(
            data["LastModifiedTime"]
        )
    else:
        raise DeserializationError("EvaluationSummary.last_modified_time required")
    if "ContactParticipant" in data:
        import aws_sdk_connect.types.evaluation_contact_participant

        out["contact_participant"] = (
            aws_sdk_connect.types.evaluation_contact_participant.deserialize_json(
                data["ContactParticipant"]
            )
        )
    return out
