"""Generated from Smithy shape ``com.amazonaws.auditmanager#Settings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_auditmanager.types.assessment_reports_destination
    import aws_sdk_auditmanager.types.boolean
    import aws_sdk_auditmanager.types.default_export_destination
    import aws_sdk_auditmanager.types.deregistration_policy
    import aws_sdk_auditmanager.types.evidence_finder_enablement
    import aws_sdk_auditmanager.types.kms_key
    import aws_sdk_auditmanager.types.roles
    import aws_sdk_auditmanager.types.sns_topic


class Settings(TypedDict, closed=True):
    is_aws_org_enabled: NotRequired["aws_sdk_auditmanager.types.boolean.Boolean"]
    """<p> Specifies whether Organizations is enabled. </p>"""
    sns_topic: NotRequired["aws_sdk_auditmanager.types.sns_topic.SNSTopic"]
    """<p> The designated Amazon Simple Notification Service (Amazon SNS) topic. </p>"""
    default_assessment_reports_destination: NotRequired[
        "aws_sdk_auditmanager.types.assessment_reports_destination.AssessmentReportsDestination"
    ]
    """<p>The default S3 destination bucket for storing assessment reports.</p>"""
    default_process_owners: NotRequired["aws_sdk_auditmanager.types.roles.Roles"]
    """<p> The designated default audit owners. </p>"""
    kms_key: NotRequired["aws_sdk_auditmanager.types.kms_key.KmsKey"]
    """<p> The KMS key details. </p>"""
    evidence_finder_enablement: NotRequired[
        "aws_sdk_auditmanager.types.evidence_finder_enablement.EvidenceFinderEnablement"
    ]
    """<p>The current evidence finder status and event data store details.</p>"""
    deregistration_policy: NotRequired[
        "aws_sdk_auditmanager.types.deregistration_policy.DeregistrationPolicy"
    ]
    """<p>The deregistration policy for your Audit Manager data. You can use this attribute to determine how your data is handled when you deregister Audit Manager.</p>"""
    default_export_destination: NotRequired[
        "aws_sdk_auditmanager.types.default_export_destination.DefaultExportDestination"
    ]
    """<p>The default S3 destination bucket for storing evidence finder exports.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Settings) -> dict:
    out: dict = {}
    if "is_aws_org_enabled" in value:
        out["isAwsOrgEnabled"] = value["is_aws_org_enabled"]
    if "sns_topic" in value:
        out["snsTopic"] = value["sns_topic"]
    if "default_assessment_reports_destination" in value:
        import aws_sdk_auditmanager.types.assessment_reports_destination

        out["defaultAssessmentReportsDestination"] = (
            aws_sdk_auditmanager.types.assessment_reports_destination.serialize_json(
                value["default_assessment_reports_destination"]
            )
        )
    if "default_process_owners" in value:
        import aws_sdk_auditmanager.types.roles

        out["defaultProcessOwners"] = aws_sdk_auditmanager.types.roles.serialize_json(
            value["default_process_owners"]
        )
    if "kms_key" in value:
        out["kmsKey"] = value["kms_key"]
    if "evidence_finder_enablement" in value:
        import aws_sdk_auditmanager.types.evidence_finder_enablement

        out["evidenceFinderEnablement"] = (
            aws_sdk_auditmanager.types.evidence_finder_enablement.serialize_json(
                value["evidence_finder_enablement"]
            )
        )
    if "deregistration_policy" in value:
        import aws_sdk_auditmanager.types.deregistration_policy

        out["deregistrationPolicy"] = (
            aws_sdk_auditmanager.types.deregistration_policy.serialize_json(
                value["deregistration_policy"]
            )
        )
    if "default_export_destination" in value:
        import aws_sdk_auditmanager.types.default_export_destination

        out["defaultExportDestination"] = (
            aws_sdk_auditmanager.types.default_export_destination.serialize_json(
                value["default_export_destination"]
            )
        )
    return out


def deserialize_json(data: dict) -> Settings:
    out: Settings = {}  # type: ignore[typeddict-item]
    if "isAwsOrgEnabled" in data:
        out["is_aws_org_enabled"] = data["isAwsOrgEnabled"]
    if "snsTopic" in data:
        out["sns_topic"] = data["snsTopic"]
    if "defaultAssessmentReportsDestination" in data:
        import aws_sdk_auditmanager.types.assessment_reports_destination

        out["default_assessment_reports_destination"] = (
            aws_sdk_auditmanager.types.assessment_reports_destination.deserialize_json(
                data["defaultAssessmentReportsDestination"]
            )
        )
    if "defaultProcessOwners" in data:
        import aws_sdk_auditmanager.types.roles

        out["default_process_owners"] = (
            aws_sdk_auditmanager.types.roles.deserialize_json(
                data["defaultProcessOwners"]
            )
        )
    if "kmsKey" in data:
        out["kms_key"] = data["kmsKey"]
    if "evidenceFinderEnablement" in data:
        import aws_sdk_auditmanager.types.evidence_finder_enablement

        out["evidence_finder_enablement"] = (
            aws_sdk_auditmanager.types.evidence_finder_enablement.deserialize_json(
                data["evidenceFinderEnablement"]
            )
        )
    if "deregistrationPolicy" in data:
        import aws_sdk_auditmanager.types.deregistration_policy

        out["deregistration_policy"] = (
            aws_sdk_auditmanager.types.deregistration_policy.deserialize_json(
                data["deregistrationPolicy"]
            )
        )
    if "defaultExportDestination" in data:
        import aws_sdk_auditmanager.types.default_export_destination

        out["default_export_destination"] = (
            aws_sdk_auditmanager.types.default_export_destination.deserialize_json(
                data["defaultExportDestination"]
            )
        )
    return out
