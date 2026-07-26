"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationSearchMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.arn
    import capo_connect.types.auto_evaluation_status
    import capo_connect.types.boolean
    import capo_connect.types.contact_id
    import capo_connect.types.contact_participant_role
    import capo_connect.types.evaluation_acknowledger_comment_string
    import capo_connect.types.evaluation_score_percentage
    import capo_connect.types.resource_id
    import capo_connect.types.timestamp


class EvaluationSearchMetadata(TypedDict, closed=True):
    contact_id: "capo_connect.types.contact_id.ContactId"
    """<p>The identifier of the contact in this instance of Connect Customer. </p>"""
    evaluator_arn: "capo_connect.types.arn.ARN"
    """<p>The Amazon Resource Name (ARN) of the person who evaluated the contact.</p>"""
    contact_agent_id: NotRequired["capo_connect.types.resource_id.ResourceId"]
    """<p>The unique ID of the agent who handled the contact.</p>"""
    calibration_session_id: NotRequired["capo_connect.types.resource_id.ResourceId"]
    """<p>The calibration session ID that this evaluation belongs to.</p>"""
    score_percentage: (
        "capo_connect.types.evaluation_score_percentage.EvaluationScorePercentage"
    )
    """<p>The total evaluation score expressed as a percentage.</p>"""
    score_automatic_fail: "capo_connect.types.boolean.Boolean"
    """<p>The flag that marks the item as automatic fail. If the item or a child item gets an automatic fail answer, this flag is true.</p>"""
    score_not_applicable: "capo_connect.types.boolean.Boolean"
    """<p>The flag to mark the item as not applicable for scoring.</p>"""
    auto_evaluation_enabled: "capo_connect.types.boolean.Boolean"
    """<p>Whether auto-evaluation is enabled.</p>"""
    auto_evaluation_status: NotRequired[
        "capo_connect.types.auto_evaluation_status.AutoEvaluationStatus"
    ]
    """<p>The status of the contact auto evaluation. </p>"""
    acknowledged_time: NotRequired["capo_connect.types.timestamp.Timestamp"]
    """<p>When the evaluation was acknowledged by the agent.</p>"""
    acknowledged_by: NotRequired["capo_connect.types.arn.ARN"]
    """<p>The agent who acknowledged the evaluation.</p>"""
    acknowledger_comment: NotRequired[
        "capo_connect.types.evaluation_acknowledger_comment_string.EvaluationAcknowledgerCommentString"
    ]
    """<p>The comment from the agent when they acknowledged the evaluation.</p>"""
    sampling_job_id: NotRequired["capo_connect.types.resource_id.ResourceId"]
    """<p>Identifier of the sampling job.</p>"""
    review_id: NotRequired["capo_connect.types.resource_id.ResourceId"]
    """<p>Identifier for the review.</p>"""
    contact_participant_role: NotRequired[
        "capo_connect.types.contact_participant_role.ContactParticipantRole"
    ]
    """<p>Role of a contact participant in the evaluation.</p>"""
    contact_participant_id: NotRequired["capo_connect.types.resource_id.ResourceId"]
    """<p>Identifier for a contact participant in the evaluation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationSearchMetadata) -> dict:
    out: dict = {}
    out["ContactId"] = value["contact_id"]
    out["EvaluatorArn"] = value["evaluator_arn"]
    if "contact_agent_id" in value:
        out["ContactAgentId"] = value["contact_agent_id"]
    if "calibration_session_id" in value:
        out["CalibrationSessionId"] = value["calibration_session_id"]
    out["ScorePercentage"] = value.get("score_percentage", 0)
    out["ScoreAutomaticFail"] = value.get("score_automatic_fail", False)
    out["ScoreNotApplicable"] = value.get("score_not_applicable", False)
    out["AutoEvaluationEnabled"] = value.get("auto_evaluation_enabled", False)
    if "auto_evaluation_status" in value:
        import capo_connect.types.auto_evaluation_status

        out["AutoEvaluationStatus"] = (
            capo_connect.types.auto_evaluation_status.serialize_json(
                value["auto_evaluation_status"]
            )
        )
    if "acknowledged_time" in value:
        import capo_connect.types.timestamp

        out["AcknowledgedTime"] = capo_connect.types.timestamp.serialize_json(
            value["acknowledged_time"]
        )
    if "acknowledged_by" in value:
        out["AcknowledgedBy"] = value["acknowledged_by"]
    if "acknowledger_comment" in value:
        out["AcknowledgerComment"] = value["acknowledger_comment"]
    if "sampling_job_id" in value:
        out["SamplingJobId"] = value["sampling_job_id"]
    if "review_id" in value:
        out["ReviewId"] = value["review_id"]
    if "contact_participant_role" in value:
        import capo_connect.types.contact_participant_role

        out["ContactParticipantRole"] = (
            capo_connect.types.contact_participant_role.serialize_json(
                value["contact_participant_role"]
            )
        )
    if "contact_participant_id" in value:
        out["ContactParticipantId"] = value["contact_participant_id"]
    return out


def deserialize_json(data: dict) -> EvaluationSearchMetadata:
    out: EvaluationSearchMetadata = {}  # type: ignore[typeddict-item]
    if "ContactId" in data:
        out["contact_id"] = data["ContactId"]
    else:
        raise DeserializationError("EvaluationSearchMetadata.contact_id required")
    if "EvaluatorArn" in data:
        out["evaluator_arn"] = data["EvaluatorArn"]
    else:
        raise DeserializationError("EvaluationSearchMetadata.evaluator_arn required")
    if "ContactAgentId" in data:
        out["contact_agent_id"] = data["ContactAgentId"]
    if "CalibrationSessionId" in data:
        out["calibration_session_id"] = data["CalibrationSessionId"]
    if "ScorePercentage" in data:
        out["score_percentage"] = data["ScorePercentage"]
    else:
        out["score_percentage"] = 0
    if "ScoreAutomaticFail" in data:
        out["score_automatic_fail"] = data["ScoreAutomaticFail"]
    else:
        out["score_automatic_fail"] = False
    if "ScoreNotApplicable" in data:
        out["score_not_applicable"] = data["ScoreNotApplicable"]
    else:
        out["score_not_applicable"] = False
    if "AutoEvaluationEnabled" in data:
        out["auto_evaluation_enabled"] = data["AutoEvaluationEnabled"]
    else:
        out["auto_evaluation_enabled"] = False
    if "AutoEvaluationStatus" in data:
        import capo_connect.types.auto_evaluation_status

        out["auto_evaluation_status"] = (
            capo_connect.types.auto_evaluation_status.deserialize_json(
                data["AutoEvaluationStatus"]
            )
        )
    if "AcknowledgedTime" in data:
        import capo_connect.types.timestamp

        out["acknowledged_time"] = capo_connect.types.timestamp.deserialize_json(
            data["AcknowledgedTime"]
        )
    if "AcknowledgedBy" in data:
        out["acknowledged_by"] = data["AcknowledgedBy"]
    if "AcknowledgerComment" in data:
        out["acknowledger_comment"] = data["AcknowledgerComment"]
    if "SamplingJobId" in data:
        out["sampling_job_id"] = data["SamplingJobId"]
    if "ReviewId" in data:
        out["review_id"] = data["ReviewId"]
    if "ContactParticipantRole" in data:
        import capo_connect.types.contact_participant_role

        out["contact_participant_role"] = (
            capo_connect.types.contact_participant_role.deserialize_json(
                data["ContactParticipantRole"]
            )
        )
    if "ContactParticipantId" in data:
        out["contact_participant_id"] = data["ContactParticipantId"]
    return out
