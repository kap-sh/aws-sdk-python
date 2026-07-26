"""Generated from Smithy shape ``com.amazonaws.auditmanager#CreateAssessmentReportResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_auditmanager.types.assessment_report


class CreateAssessmentReportResponse(TypedDict, closed=True):
    assessment_report: NotRequired[
        "capo_auditmanager.types.assessment_report.AssessmentReport"
    ]
    """<p> The new assessment report that the <code>CreateAssessmentReport</code> API returned. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAssessmentReportResponse) -> dict:
    out: dict = {}
    if "assessment_report" in value:
        import capo_auditmanager.types.assessment_report

        out["assessmentReport"] = (
            capo_auditmanager.types.assessment_report.serialize_json(
                value["assessment_report"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateAssessmentReportResponse:
    out: CreateAssessmentReportResponse = {}  # type: ignore[typeddict-item]
    if "assessmentReport" in data:
        import capo_auditmanager.types.assessment_report

        out["assessment_report"] = (
            capo_auditmanager.types.assessment_report.deserialize_json(
                data["assessmentReport"]
            )
        )
    return out
