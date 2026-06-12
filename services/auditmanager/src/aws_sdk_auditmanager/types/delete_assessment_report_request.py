"""Generated from Smithy shape ``com.amazonaws.auditmanager#DeleteAssessmentReportRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_auditmanager.types.uuid


class DeleteAssessmentReportRequest(TypedDict):
    assessment_id: "aws_sdk_auditmanager.types.uuid.UUID"
    """<p> The unique identifier for the assessment. </p>"""
    assessment_report_id: "aws_sdk_auditmanager.types.uuid.UUID"
    """<p> The unique identifier for the assessment report. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteAssessmentReportRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteAssessmentReportRequest:
    out: DeleteAssessmentReportRequest = {}  # type: ignore[typeddict-item]
    return out
