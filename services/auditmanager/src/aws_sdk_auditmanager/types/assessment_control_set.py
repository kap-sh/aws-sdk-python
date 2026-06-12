"""Generated from Smithy shape ``com.amazonaws.auditmanager#AssessmentControlSet``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_auditmanager.types.assessment_controls
    import aws_sdk_auditmanager.types.control_set_id
    import aws_sdk_auditmanager.types.control_set_status
    import aws_sdk_auditmanager.types.delegations
    import aws_sdk_auditmanager.types.integer
    import aws_sdk_auditmanager.types.non_empty_string
    import aws_sdk_auditmanager.types.roles


class AssessmentControlSet(TypedDict):
    id: NotRequired["aws_sdk_auditmanager.types.control_set_id.ControlSetId"]
    """<p> The identifier of the control set in the assessment. This is the control set name in a plain string format. </p>"""
    description: NotRequired[
        "aws_sdk_auditmanager.types.non_empty_string.NonEmptyString"
    ]
    """<p> The description for the control set. </p>"""
    status: NotRequired[
        "aws_sdk_auditmanager.types.control_set_status.ControlSetStatus"
    ]
    """<p> The current status of the control set. </p>"""
    roles: NotRequired["aws_sdk_auditmanager.types.roles.Roles"]
    """<p> The roles that are associated with the control set. </p>"""
    controls: NotRequired[
        "aws_sdk_auditmanager.types.assessment_controls.AssessmentControls"
    ]
    """<p> The list of controls that's contained with the control set. </p>"""
    delegations: NotRequired["aws_sdk_auditmanager.types.delegations.Delegations"]
    """<p> The delegations that are associated with the control set. </p>"""
    system_evidence_count: "aws_sdk_auditmanager.types.integer.Integer"
    """<p> The total number of evidence objects that are retrieved automatically for the control set. </p>"""
    manual_evidence_count: "aws_sdk_auditmanager.types.integer.Integer"
    """<p> The total number of evidence objects that are uploaded manually to the control set. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssessmentControlSet) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "description" in value:
        out["description"] = value["description"]
    if "status" in value:
        import aws_sdk_auditmanager.types.control_set_status

        out["status"] = aws_sdk_auditmanager.types.control_set_status.serialize_json(
            value["status"]
        )
    if "roles" in value:
        import aws_sdk_auditmanager.types.roles

        out["roles"] = aws_sdk_auditmanager.types.roles.serialize_json(value["roles"])
    if "controls" in value:
        import aws_sdk_auditmanager.types.assessment_controls

        out["controls"] = aws_sdk_auditmanager.types.assessment_controls.serialize_json(
            value["controls"]
        )
    if "delegations" in value:
        import aws_sdk_auditmanager.types.delegations

        out["delegations"] = aws_sdk_auditmanager.types.delegations.serialize_json(
            value["delegations"]
        )
    out["systemEvidenceCount"] = value.get("system_evidence_count", 0)
    out["manualEvidenceCount"] = value.get("manual_evidence_count", 0)
    return out


def deserialize_json(data: dict) -> AssessmentControlSet:
    out: AssessmentControlSet = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "description" in data:
        out["description"] = data["description"]
    if "status" in data:
        import aws_sdk_auditmanager.types.control_set_status

        out["status"] = aws_sdk_auditmanager.types.control_set_status.deserialize_json(
            data["status"]
        )
    if "roles" in data:
        import aws_sdk_auditmanager.types.roles

        out["roles"] = aws_sdk_auditmanager.types.roles.deserialize_json(data["roles"])
    if "controls" in data:
        import aws_sdk_auditmanager.types.assessment_controls

        out["controls"] = (
            aws_sdk_auditmanager.types.assessment_controls.deserialize_json(
                data["controls"]
            )
        )
    if "delegations" in data:
        import aws_sdk_auditmanager.types.delegations

        out["delegations"] = aws_sdk_auditmanager.types.delegations.deserialize_json(
            data["delegations"]
        )
    if "systemEvidenceCount" in data:
        out["system_evidence_count"] = data["systemEvidenceCount"]
    else:
        out["system_evidence_count"] = 0
    if "manualEvidenceCount" in data:
        out["manual_evidence_count"] = data["manualEvidenceCount"]
    else:
        out["manual_evidence_count"] = 0
    return out
