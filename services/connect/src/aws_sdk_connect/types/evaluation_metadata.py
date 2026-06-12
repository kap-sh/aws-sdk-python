"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationMetadata``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.arn
    import aws_sdk_connect.types.auto_evaluation_details
    import aws_sdk_connect.types.contact_id
    import aws_sdk_connect.types.evaluation_acknowledgement
    import aws_sdk_connect.types.evaluation_contact_participant
    import aws_sdk_connect.types.evaluation_review_metadata
    import aws_sdk_connect.types.evaluation_score
    import aws_sdk_connect.types.resource_id


class EvaluationMetadata(TypedDict):
    contact_id: "aws_sdk_connect.types.contact_id.ContactId"
    """<p>The identifier of the contact in this instance of Connect Customer. </p>"""
    evaluator_arn: "aws_sdk_connect.types.arn.ARN"
    """<p>The Amazon Resource Name (ARN) of the user who last updated the evaluation.</p>"""
    contact_agent_id: NotRequired["aws_sdk_connect.types.resource_id.ResourceId"]
    """<p>The identifier of the agent who performed the contact.</p>"""
    calibration_session_id: NotRequired["aws_sdk_connect.types.resource_id.ResourceId"]
    """<p>The calibration session ID that this evaluation belongs to.</p>"""
    score: NotRequired["aws_sdk_connect.types.evaluation_score.EvaluationScore"]
    """<p>The overall score of the contact evaluation.</p>"""
    auto_evaluation: NotRequired[
        "aws_sdk_connect.types.auto_evaluation_details.AutoEvaluationDetails"
    ]
    """<p>Information related to automated evaluation.</p>"""
    acknowledgement: NotRequired[
        "aws_sdk_connect.types.evaluation_acknowledgement.EvaluationAcknowledgement"
    ]
    """<p>Information related to evaluation acknowledgement.</p>"""
    review: NotRequired[
        "aws_sdk_connect.types.evaluation_review_metadata.EvaluationReviewMetadata"
    ]
    """<p>Information about reviews of this evaluation.</p>"""
    contact_participant: NotRequired[
        "aws_sdk_connect.types.evaluation_contact_participant.EvaluationContactParticipant"
    ]
    """<p>Information about a contact participant in this evaluation.</p>"""
    sampling_job_id: NotRequired["aws_sdk_connect.types.resource_id.ResourceId"]
    """<p>Identifier of the sampling job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationMetadata) -> dict:
    out: dict = {}
    out["ContactId"] = value["contact_id"]
    out["EvaluatorArn"] = value["evaluator_arn"]
    if "contact_agent_id" in value:
        out["ContactAgentId"] = value["contact_agent_id"]
    if "calibration_session_id" in value:
        out["CalibrationSessionId"] = value["calibration_session_id"]
    if "score" in value:
        import aws_sdk_connect.types.evaluation_score

        out["Score"] = aws_sdk_connect.types.evaluation_score.serialize_json(
            value["score"]
        )
    if "auto_evaluation" in value:
        import aws_sdk_connect.types.auto_evaluation_details

        out["AutoEvaluation"] = (
            aws_sdk_connect.types.auto_evaluation_details.serialize_json(
                value["auto_evaluation"]
            )
        )
    if "acknowledgement" in value:
        import aws_sdk_connect.types.evaluation_acknowledgement

        out["Acknowledgement"] = (
            aws_sdk_connect.types.evaluation_acknowledgement.serialize_json(
                value["acknowledgement"]
            )
        )
    if "review" in value:
        import aws_sdk_connect.types.evaluation_review_metadata

        out["Review"] = aws_sdk_connect.types.evaluation_review_metadata.serialize_json(
            value["review"]
        )
    if "contact_participant" in value:
        import aws_sdk_connect.types.evaluation_contact_participant

        out["ContactParticipant"] = (
            aws_sdk_connect.types.evaluation_contact_participant.serialize_json(
                value["contact_participant"]
            )
        )
    if "sampling_job_id" in value:
        out["SamplingJobId"] = value["sampling_job_id"]
    return out


def deserialize_json(data: dict) -> EvaluationMetadata:
    out: EvaluationMetadata = {}  # type: ignore[typeddict-item]
    if "ContactId" in data:
        out["contact_id"] = data["ContactId"]
    else:
        raise DeserializationError("EvaluationMetadata.contact_id required")
    if "EvaluatorArn" in data:
        out["evaluator_arn"] = data["EvaluatorArn"]
    else:
        raise DeserializationError("EvaluationMetadata.evaluator_arn required")
    if "ContactAgentId" in data:
        out["contact_agent_id"] = data["ContactAgentId"]
    if "CalibrationSessionId" in data:
        out["calibration_session_id"] = data["CalibrationSessionId"]
    if "Score" in data:
        import aws_sdk_connect.types.evaluation_score

        out["score"] = aws_sdk_connect.types.evaluation_score.deserialize_json(
            data["Score"]
        )
    if "AutoEvaluation" in data:
        import aws_sdk_connect.types.auto_evaluation_details

        out["auto_evaluation"] = (
            aws_sdk_connect.types.auto_evaluation_details.deserialize_json(
                data["AutoEvaluation"]
            )
        )
    if "Acknowledgement" in data:
        import aws_sdk_connect.types.evaluation_acknowledgement

        out["acknowledgement"] = (
            aws_sdk_connect.types.evaluation_acknowledgement.deserialize_json(
                data["Acknowledgement"]
            )
        )
    if "Review" in data:
        import aws_sdk_connect.types.evaluation_review_metadata

        out["review"] = (
            aws_sdk_connect.types.evaluation_review_metadata.deserialize_json(
                data["Review"]
            )
        )
    if "ContactParticipant" in data:
        import aws_sdk_connect.types.evaluation_contact_participant

        out["contact_participant"] = (
            aws_sdk_connect.types.evaluation_contact_participant.deserialize_json(
                data["ContactParticipant"]
            )
        )
    if "SamplingJobId" in data:
        out["sampling_job_id"] = data["SamplingJobId"]
    return out
