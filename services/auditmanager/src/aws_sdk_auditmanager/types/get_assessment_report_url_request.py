"""Generated from Smithy shape ``com.amazonaws.auditmanager#GetAssessmentReportUrlRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_auditmanager.types.uuid


class GetAssessmentReportUrlRequest(TypedDict):
    assessment_report_id: "aws_sdk_auditmanager.types.uuid.UUID"
    """<p> The unique identifier for the assessment report. </p>"""
    assessment_id: "aws_sdk_auditmanager.types.uuid.UUID"
    """<p> The unique identifier for the assessment. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAssessmentReportUrlRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetAssessmentReportUrlRequest:
    out: GetAssessmentReportUrlRequest = {}  # type: ignore[typeddict-item]
    return out
