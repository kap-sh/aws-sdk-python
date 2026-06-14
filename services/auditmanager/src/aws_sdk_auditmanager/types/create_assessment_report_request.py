"""Generated from Smithy shape ``com.amazonaws.auditmanager#CreateAssessmentReportRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_auditmanager.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_auditmanager.types.assessment_report_description
    import aws_sdk_auditmanager.types.assessment_report_name
    import aws_sdk_auditmanager.types.query_statement
    import aws_sdk_auditmanager.types.uuid


class CreateAssessmentReportRequest(TypedDict):
    name: "aws_sdk_auditmanager.types.assessment_report_name.AssessmentReportName"
    """<p> The name of the new assessment report. </p>"""
    description: NotRequired[
        "aws_sdk_auditmanager.types.assessment_report_description.AssessmentReportDescription"
    ]
    """<p> The description of the assessment report. </p>"""
    assessment_id: "aws_sdk_auditmanager.types.uuid.UUID"
    """<p> The identifier for the assessment. </p>"""
    query_statement: NotRequired[
        "aws_sdk_auditmanager.types.query_statement.QueryStatement"
    ]
    r"""<p>A SQL statement that represents an evidence finder query.</p> <p>Provide this parameter when you want to generate an assessment report from the results of an evidence finder search query. When you use this parameter, Audit Manager generates a one-time report using only the evidence from the query output. This report does not include any assessment evidence that was manually <a href=\"https://docs.aws.amazon.com/audit-manager/latest/userguide/generate-assessment-report.html#generate-assessment-report-include-evidence\">added to a report using the console</a>, or <a href=\"https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_BatchAssociateAssessmentReportEvidence.html\">associated with a report using the API</a>. </p> <p>To use this parameter, the <a href=\"https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_EvidenceFinderEnablement.html#auditmanager-Type-EvidenceFinderEnablement-enablementStatus\">enablementStatus</a> of evidence finder must be <code>ENABLED</code>. </p> <p> For examples and help resolving <code>queryStatement</code> validation exceptions, see <a href=\"https://docs.aws.amazon.com/audit-manager/latest/userguide/evidence-finder-issues.html#querystatement-exceptions\">Troubleshooting evidence finder issues</a> in the <i>Audit Manager User Guide.</i> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAssessmentReportRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "query_statement" in value:
        out["queryStatement"] = value["query_statement"]
    return out


def deserialize_json(data: dict) -> CreateAssessmentReportRequest:
    out: CreateAssessmentReportRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateAssessmentReportRequest.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "queryStatement" in data:
        out["query_statement"] = data["queryStatement"]
    return out
