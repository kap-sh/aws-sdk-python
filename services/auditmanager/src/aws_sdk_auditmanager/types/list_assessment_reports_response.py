"""Generated from Smithy shape ``com.amazonaws.auditmanager#ListAssessmentReportsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_auditmanager.types.assessment_reports_metadata
    import aws_sdk_auditmanager.types.token


class ListAssessmentReportsResponse(TypedDict, closed=True):
    assessment_reports: NotRequired[
        "aws_sdk_auditmanager.types.assessment_reports_metadata.AssessmentReportsMetadata"
    ]
    """<p> The list of assessment reports that the <code>ListAssessmentReports</code> API returned. </p>"""
    next_token: NotRequired["aws_sdk_auditmanager.types.token.Token"]
    """<p> The pagination token that's used to fetch the next set of results. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAssessmentReportsResponse) -> dict:
    out: dict = {}
    if "assessment_reports" in value:
        import aws_sdk_auditmanager.types.assessment_reports_metadata

        out["assessmentReports"] = (
            aws_sdk_auditmanager.types.assessment_reports_metadata.serialize_json(
                value["assessment_reports"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAssessmentReportsResponse:
    out: ListAssessmentReportsResponse = {}  # type: ignore[typeddict-item]
    if "assessmentReports" in data:
        import aws_sdk_auditmanager.types.assessment_reports_metadata

        out["assessment_reports"] = (
            aws_sdk_auditmanager.types.assessment_reports_metadata.deserialize_json(
                data["assessmentReports"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
