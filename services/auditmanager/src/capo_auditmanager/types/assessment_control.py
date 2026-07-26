"""Generated from Smithy shape ``com.amazonaws.auditmanager#AssessmentControl``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_auditmanager.types.control_comments
    import capo_auditmanager.types.control_description
    import capo_auditmanager.types.control_name
    import capo_auditmanager.types.control_response
    import capo_auditmanager.types.control_status
    import capo_auditmanager.types.evidence_sources
    import capo_auditmanager.types.integer
    import capo_auditmanager.types.uuid


class AssessmentControl(TypedDict, closed=True):
    id: NotRequired["capo_auditmanager.types.uuid.UUID"]
    """<p> The identifier for the control. </p>"""
    name: NotRequired["capo_auditmanager.types.control_name.ControlName"]
    """<p> The name of the control. </p>"""
    description: NotRequired[
        "capo_auditmanager.types.control_description.ControlDescription"
    ]
    """<p> The description of the control. </p>"""
    status: NotRequired["capo_auditmanager.types.control_status.ControlStatus"]
    """<p> The status of the control. </p>"""
    response: NotRequired["capo_auditmanager.types.control_response.ControlResponse"]
    """<p> The response of the control. </p>"""
    comments: NotRequired["capo_auditmanager.types.control_comments.ControlComments"]
    """<p> The list of comments that's attached to the control. </p>"""
    evidence_sources: NotRequired[
        "capo_auditmanager.types.evidence_sources.EvidenceSources"
    ]
    """<p> The list of data sources for the evidence. </p>"""
    evidence_count: "capo_auditmanager.types.integer.Integer"
    """<p> The amount of evidence that's collected for the control. </p>"""
    assessment_report_evidence_count: "capo_auditmanager.types.integer.Integer"
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
        import capo_auditmanager.types.control_status

        out["status"] = capo_auditmanager.types.control_status.serialize_json(
            value["status"]
        )
    if "response" in value:
        import capo_auditmanager.types.control_response

        out["response"] = capo_auditmanager.types.control_response.serialize_json(
            value["response"]
        )
    if "comments" in value:
        import capo_auditmanager.types.control_comments

        out["comments"] = capo_auditmanager.types.control_comments.serialize_json(
            value["comments"]
        )
    if "evidence_sources" in value:
        import capo_auditmanager.types.evidence_sources

        out["evidenceSources"] = (
            capo_auditmanager.types.evidence_sources.serialize_json(
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
        import capo_auditmanager.types.control_status

        out["status"] = capo_auditmanager.types.control_status.deserialize_json(
            data["status"]
        )
    if "response" in data:
        import capo_auditmanager.types.control_response

        out["response"] = capo_auditmanager.types.control_response.deserialize_json(
            data["response"]
        )
    if "comments" in data:
        import capo_auditmanager.types.control_comments

        out["comments"] = capo_auditmanager.types.control_comments.deserialize_json(
            data["comments"]
        )
    if "evidenceSources" in data:
        import capo_auditmanager.types.evidence_sources

        out["evidence_sources"] = (
            capo_auditmanager.types.evidence_sources.deserialize_json(
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
