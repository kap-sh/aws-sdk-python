"""Generated from Smithy shape ``com.amazonaws.auditmanager#AssessmentMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_auditmanager.types.assessment_description
    import aws_sdk_auditmanager.types.assessment_name
    import aws_sdk_auditmanager.types.assessment_reports_destination
    import aws_sdk_auditmanager.types.assessment_status
    import aws_sdk_auditmanager.types.compliance_type
    import aws_sdk_auditmanager.types.delegations
    import aws_sdk_auditmanager.types.roles
    import aws_sdk_auditmanager.types.scope
    import aws_sdk_auditmanager.types.timestamp
    import aws_sdk_auditmanager.types.uuid


class AssessmentMetadata(TypedDict, closed=True):
    name: NotRequired["aws_sdk_auditmanager.types.assessment_name.AssessmentName"]
    """<p> The name of the assessment. </p>"""
    id: NotRequired["aws_sdk_auditmanager.types.uuid.UUID"]
    """<p> The unique identifier for the assessment. </p>"""
    description: NotRequired[
        "aws_sdk_auditmanager.types.assessment_description.AssessmentDescription"
    ]
    """<p> The description of the assessment. </p>"""
    compliance_type: NotRequired[
        "aws_sdk_auditmanager.types.compliance_type.ComplianceType"
    ]
    """<p> The name of the compliance standard that's related to the assessment, such as PCI-DSS. </p>"""
    status: NotRequired["aws_sdk_auditmanager.types.assessment_status.AssessmentStatus"]
    """<p> The overall status of the assessment. </p>"""
    assessment_reports_destination: NotRequired[
        "aws_sdk_auditmanager.types.assessment_reports_destination.AssessmentReportsDestination"
    ]
    """<p> The destination that evidence reports are stored in for the assessment. </p>"""
    scope: NotRequired["aws_sdk_auditmanager.types.scope.Scope"]
    """<p> The wrapper of Amazon Web Services accounts and services that are in scope for the assessment. </p>"""
    roles: NotRequired["aws_sdk_auditmanager.types.roles.Roles"]
    """<p> The roles that are associated with the assessment. </p>"""
    delegations: NotRequired["aws_sdk_auditmanager.types.delegations.Delegations"]
    """<p> The delegations that are associated with the assessment. </p>"""
    creation_time: NotRequired["aws_sdk_auditmanager.types.timestamp.Timestamp"]
    """<p> Specifies when the assessment was created. </p>"""
    last_updated: NotRequired["aws_sdk_auditmanager.types.timestamp.Timestamp"]
    """<p> The time of the most recent update. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssessmentMetadata) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "id" in value:
        out["id"] = value["id"]
    if "description" in value:
        out["description"] = value["description"]
    if "compliance_type" in value:
        out["complianceType"] = value["compliance_type"]
    if "status" in value:
        import aws_sdk_auditmanager.types.assessment_status

        out["status"] = aws_sdk_auditmanager.types.assessment_status.serialize_json(
            value["status"]
        )
    if "assessment_reports_destination" in value:
        import aws_sdk_auditmanager.types.assessment_reports_destination

        out["assessmentReportsDestination"] = (
            aws_sdk_auditmanager.types.assessment_reports_destination.serialize_json(
                value["assessment_reports_destination"]
            )
        )
    if "scope" in value:
        import aws_sdk_auditmanager.types.scope

        out["scope"] = aws_sdk_auditmanager.types.scope.serialize_json(value["scope"])
    if "roles" in value:
        import aws_sdk_auditmanager.types.roles

        out["roles"] = aws_sdk_auditmanager.types.roles.serialize_json(value["roles"])
    if "delegations" in value:
        import aws_sdk_auditmanager.types.delegations

        out["delegations"] = aws_sdk_auditmanager.types.delegations.serialize_json(
            value["delegations"]
        )
    if "creation_time" in value:
        import aws_sdk_auditmanager.types.timestamp

        out["creationTime"] = aws_sdk_auditmanager.types.timestamp.serialize_json(
            value["creation_time"]
        )
    if "last_updated" in value:
        import aws_sdk_auditmanager.types.timestamp

        out["lastUpdated"] = aws_sdk_auditmanager.types.timestamp.serialize_json(
            value["last_updated"]
        )
    return out


def deserialize_json(data: dict) -> AssessmentMetadata:
    out: AssessmentMetadata = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "id" in data:
        out["id"] = data["id"]
    if "description" in data:
        out["description"] = data["description"]
    if "complianceType" in data:
        out["compliance_type"] = data["complianceType"]
    if "status" in data:
        import aws_sdk_auditmanager.types.assessment_status

        out["status"] = aws_sdk_auditmanager.types.assessment_status.deserialize_json(
            data["status"]
        )
    if "assessmentReportsDestination" in data:
        import aws_sdk_auditmanager.types.assessment_reports_destination

        out["assessment_reports_destination"] = (
            aws_sdk_auditmanager.types.assessment_reports_destination.deserialize_json(
                data["assessmentReportsDestination"]
            )
        )
    if "scope" in data:
        import aws_sdk_auditmanager.types.scope

        out["scope"] = aws_sdk_auditmanager.types.scope.deserialize_json(data["scope"])
    if "roles" in data:
        import aws_sdk_auditmanager.types.roles

        out["roles"] = aws_sdk_auditmanager.types.roles.deserialize_json(data["roles"])
    if "delegations" in data:
        import aws_sdk_auditmanager.types.delegations

        out["delegations"] = aws_sdk_auditmanager.types.delegations.deserialize_json(
            data["delegations"]
        )
    if "creationTime" in data:
        import aws_sdk_auditmanager.types.timestamp

        out["creation_time"] = aws_sdk_auditmanager.types.timestamp.deserialize_json(
            data["creationTime"]
        )
    if "lastUpdated" in data:
        import aws_sdk_auditmanager.types.timestamp

        out["last_updated"] = aws_sdk_auditmanager.types.timestamp.deserialize_json(
            data["lastUpdated"]
        )
    return out
