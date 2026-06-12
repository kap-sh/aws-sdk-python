"""Generated from Smithy shape ``com.amazonaws.auditmanager#UpdateAssessmentControlSetStatusRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_auditmanager.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_auditmanager.types.control_set_status
    import aws_sdk_auditmanager.types.delegation_comment
    import aws_sdk_auditmanager.types.string
    import aws_sdk_auditmanager.types.uuid


class UpdateAssessmentControlSetStatusRequest(TypedDict):
    assessment_id: "aws_sdk_auditmanager.types.uuid.UUID"
    """<p> The unique identifier for the assessment. </p>"""
    control_set_id: "aws_sdk_auditmanager.types.string.String"
    """<p> The unique identifier for the control set. </p>"""
    status: "aws_sdk_auditmanager.types.control_set_status.ControlSetStatus"
    """<p> The status of the control set that's being updated. </p>"""
    comment: "aws_sdk_auditmanager.types.delegation_comment.DelegationComment"
    """<p> The comment that's related to the status update. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAssessmentControlSetStatusRequest) -> dict:
    out: dict = {}
    import aws_sdk_auditmanager.types.control_set_status

    out["status"] = aws_sdk_auditmanager.types.control_set_status.serialize_json(
        value["status"]
    )
    out["comment"] = value["comment"]
    return out


def deserialize_json(data: dict) -> UpdateAssessmentControlSetStatusRequest:
    out: UpdateAssessmentControlSetStatusRequest = {}  # type: ignore[typeddict-item]
    if "status" in data:
        import aws_sdk_auditmanager.types.control_set_status

        out["status"] = aws_sdk_auditmanager.types.control_set_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError(
            "UpdateAssessmentControlSetStatusRequest.status required"
        )
    if "comment" in data:
        out["comment"] = data["comment"]
    else:
        raise DeserializationError(
            "UpdateAssessmentControlSetStatusRequest.comment required"
        )
    return out
