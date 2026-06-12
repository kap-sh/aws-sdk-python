"""Generated from Smithy shape ``com.amazonaws.auditmanager#AssessmentControl``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_auditmanager.types.control_comments
    import aws_sdk_auditmanager.types.control_description
    import aws_sdk_auditmanager.types.control_name
    import aws_sdk_auditmanager.types.control_response
    import aws_sdk_auditmanager.types.control_status
    import aws_sdk_auditmanager.types.evidence_sources
    import aws_sdk_auditmanager.types.integer
    import aws_sdk_auditmanager.types.uuid


class AssessmentControl(TypedDict):
    id: NotRequired["aws_sdk_auditmanager.types.uuid.UUID"]
    """<p> The identifier for the control. </p>"""
    name: NotRequired["aws_sdk_auditmanager.types.control_name.ControlName"]
    """<p> The name of the control. </p>"""
    description: NotRequired[
        "aws_sdk_auditmanager.types.control_description.ControlDescription"
    ]
    """<p> The description of the control. </p>"""
    status: NotRequired["aws_sdk_auditmanager.types.control_status.ControlStatus"]
    """<p> The status of the control. </p>"""
    response: NotRequired["aws_sdk_auditmanager.types.control_response.ControlResponse"]
    """<p> The response of the control. </p>"""
    comments: NotRequired["aws_sdk_auditmanager.types.control_comments.ControlComments"]
    """<p> The list of comments that's attached to the control. </p>"""
    evidence_sources: NotRequired[
        "aws_sdk_auditmanager.types.evidence_sources.EvidenceSources"
    ]
    """<p> The list of data sources for the evidence. </p>"""
    evidence_count: "aws_sdk_auditmanager.types.integer.Integer"
    """<p> The amount of evidence that's collected for the control. </p>"""
    assessment_report_evidence_count: "aws_sdk_auditmanager.types.integer.Integer"
    """<p> The amount of evidence in the assessment report. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssessmentControl) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "status" in value:
        import aws_sdk_auditmanager.types.control_status

        out["status"] = aws_sdk_auditmanager.types.control_status.serialize_json(
            value["status"]
        )
    if "response" in value:
        import aws_sdk_auditmanager.types.control_response

        out["response"] = aws_sdk_auditmanager.types.control_response.serialize_json(
            value["response"]
        )
    if "comments" in value:
        import aws_sdk_auditmanager.types.control_comments

        out["comments"] = aws_sdk_auditmanager.types.control_comments.serialize_json(
            value["comments"]
        )
    if "evidence_sources" in value:
        import aws_sdk_auditmanager.types.evidence_sources

        out["evidenceSources"] = (
            aws_sdk_auditmanager.types.evidence_sources.serialize_json(
                value["evidence_sources"]
            )
        )
    out["evidenceCount"] = value.get("evidence_count", 0)
    out["assessmentReportEvidenceCount"] = value.get(
        "assessment_report_evidence_count", 0
    )
    return out


def deserialize_json(data: dict) -> AssessmentControl:
    out: AssessmentControl = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "name" in data:
        out["name"] = data["name"]
    if "description" in data:
        out["description"] = data["description"]
    if "status" in data:
        import aws_sdk_auditmanager.types.control_status

        out["status"] = aws_sdk_auditmanager.types.control_status.deserialize_json(
            data["status"]
        )
    if "response" in data:
        import aws_sdk_auditmanager.types.control_response

        out["response"] = aws_sdk_auditmanager.types.control_response.deserialize_json(
            data["response"]
        )
    if "comments" in data:
        import aws_sdk_auditmanager.types.control_comments

        out["comments"] = aws_sdk_auditmanager.types.control_comments.deserialize_json(
            data["comments"]
        )
    if "evidenceSources" in data:
        import aws_sdk_auditmanager.types.evidence_sources

        out["evidence_sources"] = (
            aws_sdk_auditmanager.types.evidence_sources.deserialize_json(
                data["evidenceSources"]
            )
        )
    if "evidenceCount" in data:
        out["evidence_count"] = data["evidenceCount"]
    else:
        out["evidence_count"] = 0
    if "assessmentReportEvidenceCount" in data:
        out["assessment_report_evidence_count"] = data["assessmentReportEvidenceCount"]
    else:
        out["assessment_report_evidence_count"] = 0
    return out
