"""Generated from Smithy shape ``com.amazonaws.auditmanager#AssessmentEvidenceFolder``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_auditmanager.types.assessment_evidence_folder_name
    import aws_sdk_auditmanager.types.control_name
    import aws_sdk_auditmanager.types.control_set_id
    import aws_sdk_auditmanager.types.integer
    import aws_sdk_auditmanager.types.string
    import aws_sdk_auditmanager.types.timestamp
    import aws_sdk_auditmanager.types.uuid


class AssessmentEvidenceFolder(TypedDict, closed=True):
    name: NotRequired[
        "aws_sdk_auditmanager.types.assessment_evidence_folder_name.AssessmentEvidenceFolderName"
    ]
    """<p> The name of the evidence folder. </p>"""
    date: NotRequired["aws_sdk_auditmanager.types.timestamp.Timestamp"]
    """<p> The date when the first evidence was added to the evidence folder. </p>"""
    assessment_id: NotRequired["aws_sdk_auditmanager.types.uuid.UUID"]
    """<p> The identifier for the assessment. </p>"""
    control_set_id: NotRequired[
        "aws_sdk_auditmanager.types.control_set_id.ControlSetId"
    ]
    """<p> The identifier for the control set. </p>"""
    control_id: NotRequired["aws_sdk_auditmanager.types.uuid.UUID"]
    """<p> The unique identifier for the control. </p>"""
    id: NotRequired["aws_sdk_auditmanager.types.uuid.UUID"]
    """<p> The identifier for the folder that the evidence is stored in. </p>"""
    data_source: NotRequired["aws_sdk_auditmanager.types.string.String"]
    """<p> The Amazon Web Services service that the evidence was collected from. </p>"""
    author: NotRequired["aws_sdk_auditmanager.types.string.String"]
    """<p> The name of the user who created the evidence folder. </p>"""
    total_evidence: "aws_sdk_auditmanager.types.integer.Integer"
    """<p> The total amount of evidence in the evidence folder. </p>"""
    assessment_report_selection_count: "aws_sdk_auditmanager.types.integer.Integer"
    """<p> The total count of evidence that's included in the assessment report. </p>"""
    control_name: NotRequired["aws_sdk_auditmanager.types.control_name.ControlName"]
    """<p> The name of the control. </p>"""
    evidence_resources_included_count: "aws_sdk_auditmanager.types.integer.Integer"
    """<p> The amount of evidence that's included in the evidence folder. </p>"""
    evidence_by_type_configuration_data_count: (
        "aws_sdk_auditmanager.types.integer.Integer"
    )
    """<p> The number of evidence that falls under the configuration data category. This evidence is collected from configuration snapshots of other Amazon Web Services services such as Amazon EC2, Amazon S3, or IAM. </p>"""
    evidence_by_type_manual_count: "aws_sdk_auditmanager.types.integer.Integer"
    """<p> The number of evidence that falls under the manual category. This evidence is imported manually. </p>"""
    evidence_by_type_compliance_check_count: (
        "aws_sdk_auditmanager.types.integer.Integer"
    )
    """<p> The number of evidence that falls under the compliance check category. This evidence is collected from Config or Security Hub CSPM. </p>"""
    evidence_by_type_compliance_check_issues_count: (
        "aws_sdk_auditmanager.types.integer.Integer"
    )
    """<p> The total number of issues that were reported directly from Security Hub CSPM, Config, or both. </p>"""
    evidence_by_type_user_activity_count: "aws_sdk_auditmanager.types.integer.Integer"
    """<p> The number of evidence that falls under the user activity category. This evidence is collected from CloudTrail logs. </p>"""
    evidence_aws_service_source_count: "aws_sdk_auditmanager.types.integer.Integer"
    """<p> The total number of Amazon Web Services resources that were assessed to generate the evidence. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssessmentEvidenceFolder) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "date" in value:
        import aws_sdk_auditmanager.types.timestamp

        out["date"] = aws_sdk_auditmanager.types.timestamp.serialize_json(value["date"])
    if "assessment_id" in value:
        out["assessmentId"] = value["assessment_id"]
    if "control_set_id" in value:
        out["controlSetId"] = value["control_set_id"]
    if "control_id" in value:
        out["controlId"] = value["control_id"]
    if "id" in value:
        out["id"] = value["id"]
    if "data_source" in value:
        out["dataSource"] = value["data_source"]
    if "author" in value:
        out["author"] = value["author"]
    out["totalEvidence"] = value.get("total_evidence", 0)
    out["assessmentReportSelectionCount"] = value.get(
        "assessment_report_selection_count", 0
    )
    if "control_name" in value:
        out["controlName"] = value["control_name"]
    out["evidenceResourcesIncludedCount"] = value.get(
        "evidence_resources_included_count", 0
    )
    out["evidenceByTypeConfigurationDataCount"] = value.get(
        "evidence_by_type_configuration_data_count", 0
    )
    out["evidenceByTypeManualCount"] = value.get("evidence_by_type_manual_count", 0)
    out["evidenceByTypeComplianceCheckCount"] = value.get(
        "evidence_by_type_compliance_check_count", 0
    )
    out["evidenceByTypeComplianceCheckIssuesCount"] = value.get(
        "evidence_by_type_compliance_check_issues_count", 0
    )
    out["evidenceByTypeUserActivityCount"] = value.get(
        "evidence_by_type_user_activity_count", 0
    )
    out["evidenceAwsServiceSourceCount"] = value.get(
        "evidence_aws_service_source_count", 0
    )
    return out


def deserialize_json(data: dict) -> AssessmentEvidenceFolder:
    out: AssessmentEvidenceFolder = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "date" in data:
        import aws_sdk_auditmanager.types.timestamp

        out["date"] = aws_sdk_auditmanager.types.timestamp.deserialize_json(
            data["date"]
        )
    if "assessmentId" in data:
        out["assessment_id"] = data["assessmentId"]
    if "controlSetId" in data:
        out["control_set_id"] = data["controlSetId"]
    if "controlId" in data:
        out["control_id"] = data["controlId"]
    if "id" in data:
        out["id"] = data["id"]
    if "dataSource" in data:
        out["data_source"] = data["dataSource"]
    if "author" in data:
        out["author"] = data["author"]
    if "totalEvidence" in data:
        out["total_evidence"] = data["totalEvidence"]
    else:
        out["total_evidence"] = 0
    if "assessmentReportSelectionCount" in data:
        out["assessment_report_selection_count"] = data[
            "assessmentReportSelectionCount"
        ]
    else:
        out["assessment_report_selection_count"] = 0
    if "controlName" in data:
        out["control_name"] = data["controlName"]
    if "evidenceResourcesIncludedCount" in data:
        out["evidence_resources_included_count"] = data[
            "evidenceResourcesIncludedCount"
        ]
    else:
        out["evidence_resources_included_count"] = 0
    if "evidenceByTypeConfigurationDataCount" in data:
        out["evidence_by_type_configuration_data_count"] = data[
            "evidenceByTypeConfigurationDataCount"
        ]
    else:
        out["evidence_by_type_configuration_data_count"] = 0
    if "evidenceByTypeManualCount" in data:
        out["evidence_by_type_manual_count"] = data["evidenceByTypeManualCount"]
    else:
        out["evidence_by_type_manual_count"] = 0
    if "evidenceByTypeComplianceCheckCount" in data:
        out["evidence_by_type_compliance_check_count"] = data[
            "evidenceByTypeComplianceCheckCount"
        ]
    else:
        out["evidence_by_type_compliance_check_count"] = 0
    if "evidenceByTypeComplianceCheckIssuesCount" in data:
        out["evidence_by_type_compliance_check_issues_count"] = data[
            "evidenceByTypeComplianceCheckIssuesCount"
        ]
    else:
        out["evidence_by_type_compliance_check_issues_count"] = 0
    if "evidenceByTypeUserActivityCount" in data:
        out["evidence_by_type_user_activity_count"] = data[
            "evidenceByTypeUserActivityCount"
        ]
    else:
        out["evidence_by_type_user_activity_count"] = 0
    if "evidenceAwsServiceSourceCount" in data:
        out["evidence_aws_service_source_count"] = data["evidenceAwsServiceSourceCount"]
    else:
        out["evidence_aws_service_source_count"] = 0
    return out
