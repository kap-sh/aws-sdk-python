"""Generated from Smithy shape ``com.amazonaws.auditmanager#UpdateAssessmentStatusRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_auditmanager.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_auditmanager.types.assessment_status
    import aws_sdk_auditmanager.types.uuid


class UpdateAssessmentStatusRequest(TypedDict):
    assessment_id: "aws_sdk_auditmanager.types.uuid.UUID"
    """<p> The unique identifier for the assessment. </p>"""
    status: "aws_sdk_auditmanager.types.assessment_status.AssessmentStatus"
    """<p> The current status of the assessment. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAssessmentStatusRequest) -> dict:
    out: dict = {}
    import aws_sdk_auditmanager.types.assessment_status

    out["status"] = aws_sdk_auditmanager.types.assessment_status.serialize_json(
        value["status"]
    )
    return out


def deserialize_json(data: dict) -> UpdateAssessmentStatusRequest:
    out: UpdateAssessmentStatusRequest = {}  # type: ignore[typeddict-item]
    if "status" in data:
        import aws_sdk_auditmanager.types.assessment_status

        out["status"] = aws_sdk_auditmanager.types.assessment_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("UpdateAssessmentStatusRequest.status required")
    return out
