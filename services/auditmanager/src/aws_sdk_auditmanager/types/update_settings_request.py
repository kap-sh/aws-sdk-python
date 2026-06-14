"""Generated from Smithy shape ``com.amazonaws.auditmanager#UpdateSettingsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_auditmanager.types.assessment_reports_destination
    import aws_sdk_auditmanager.types.boolean
    import aws_sdk_auditmanager.types.default_export_destination
    import aws_sdk_auditmanager.types.deregistration_policy
    import aws_sdk_auditmanager.types.kms_key
    import aws_sdk_auditmanager.types.roles
    import aws_sdk_auditmanager.types.sns_arn


class UpdateSettingsRequest(TypedDict):
    sns_topic: NotRequired["aws_sdk_auditmanager.types.sns_arn.SnsArn"]
    """<p> The Amazon Simple Notification Service (Amazon SNS) topic that Audit Manager sends notifications to. </p>"""
    default_assessment_reports_destination: NotRequired[
        "aws_sdk_auditmanager.types.assessment_reports_destination.AssessmentReportsDestination"
    ]
    """<p> The default S3 destination bucket for storing assessment reports. </p>"""
    default_process_owners: NotRequired["aws_sdk_auditmanager.types.roles.Roles"]
    """<p> A list of the default audit owners. </p>"""
    kms_key: NotRequired["aws_sdk_auditmanager.types.kms_key.KmsKey"]
    """<p> The KMS key details. </p>"""
    evidence_finder_enabled: NotRequired["aws_sdk_auditmanager.types.boolean.Boolean"]
    r"""<p>Specifies whether the evidence finder feature is enabled. Change this attribute to enable or disable evidence finder.</p> <important> <p>When you use this attribute to disable evidence finder, Audit Manager deletes the event data store that’s used to query your evidence data. As a result, you can’t re-enable evidence finder and use the feature again. Your only alternative is to <a href=\"https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_DeregisterAccount.html\">deregister</a> and then <a href=\"https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_RegisterAccount.html\">re-register</a> Audit Manager. </p> </important>"""
    deregistration_policy: NotRequired[
        "aws_sdk_auditmanager.types.deregistration_policy.DeregistrationPolicy"
    ]
    """<p>The deregistration policy for your Audit Manager data. You can use this attribute to determine how your data is handled when you deregister Audit Manager.</p>"""
    default_export_destination: NotRequired[
        "aws_sdk_auditmanager.types.default_export_destination.DefaultExportDestination"
    ]
    """<p> The default S3 destination bucket for storing evidence finder exports. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateSettingsRequest) -> dict:
    out: dict = {}
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
    if "evidence_finder_enabled" in value:
        out["evidenceFinderEnabled"] = value["evidence_finder_enabled"]
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


def deserialize_json(data: dict) -> UpdateSettingsRequest:
    out: UpdateSettingsRequest = {}  # type: ignore[typeddict-item]
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
    if "evidenceFinderEnabled" in data:
        out["evidence_finder_enabled"] = data["evidenceFinderEnabled"]
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
