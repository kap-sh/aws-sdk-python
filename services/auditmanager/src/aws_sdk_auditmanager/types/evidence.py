"""Generated from Smithy shape ``com.amazonaws.auditmanager#Evidence``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_auditmanager.types.account_id
    import aws_sdk_auditmanager.types.aws_service_name
    import aws_sdk_auditmanager.types.event_name
    import aws_sdk_auditmanager.types.evidence_attributes
    import aws_sdk_auditmanager.types.iam_arn
    import aws_sdk_auditmanager.types.resources
    import aws_sdk_auditmanager.types.string
    import aws_sdk_auditmanager.types.timestamp
    import aws_sdk_auditmanager.types.uuid


class Evidence(TypedDict, closed=True):
    data_source: NotRequired["aws_sdk_auditmanager.types.string.String"]
    """<p> The data source where the evidence was collected from. </p>"""
    evidence_aws_account_id: NotRequired[
        "aws_sdk_auditmanager.types.account_id.AccountId"
    ]
    """<p> The identifier for the Amazon Web Services account. </p>"""
    time: NotRequired["aws_sdk_auditmanager.types.timestamp.Timestamp"]
    """<p> The timestamp that represents when the evidence was collected. </p>"""
    event_source: NotRequired[
        "aws_sdk_auditmanager.types.aws_service_name.AWSServiceName"
    ]
    """<p> The Amazon Web Services service that the evidence is collected from. </p>"""
    event_name: NotRequired["aws_sdk_auditmanager.types.event_name.EventName"]
    """<p> The name of the evidence event. </p>"""
    evidence_by_type: NotRequired["aws_sdk_auditmanager.types.string.String"]
    """<p> The type of automated evidence. </p>"""
    resources_included: NotRequired["aws_sdk_auditmanager.types.resources.Resources"]
    """<p> The list of resources that are assessed to generate the evidence. </p>"""
    attributes: NotRequired[
        "aws_sdk_auditmanager.types.evidence_attributes.EvidenceAttributes"
    ]
    """<p> The names and values that are used by the evidence event. This includes an attribute name (such as <code>allowUsersToChangePassword</code>) and value (such as <code>true</code> or <code>false</code>). </p>"""
    iam_id: NotRequired["aws_sdk_auditmanager.types.iam_arn.IamArn"]
    """<p> The unique identifier for the user or role that's associated with the evidence. </p>"""
    compliance_check: NotRequired["aws_sdk_auditmanager.types.string.String"]
    """<p>The evaluation status for automated evidence that falls under the compliance check category.</p> <ul> <li> <p>Audit Manager classes evidence as non-compliant if Security Hub CSPM reports a <i>Fail</i> result, or if Config reports a <i>Non-compliant</i> result.</p> </li> <li> <p>Audit Manager classes evidence as compliant if Security Hub CSPM reports a <i>Pass</i> result, or if Config reports a <i>Compliant</i> result.</p> </li> <li> <p>If a compliance check isn't available or applicable, then no compliance evaluation can be made for that evidence. This is the case if the evidence uses Config or Security Hub CSPM as the underlying data source type, but those services aren't enabled. This is also the case if the evidence uses an underlying data source type that doesn't support compliance checks (such as manual evidence, Amazon Web Services API calls, or CloudTrail). </p> </li> </ul>"""
    aws_organization: NotRequired["aws_sdk_auditmanager.types.string.String"]
    """<p> The Amazon Web Services account that the evidence is collected from, and its organization path. </p>"""
    aws_account_id: NotRequired["aws_sdk_auditmanager.types.account_id.AccountId"]
    """<p> The identifier for the Amazon Web Services account. </p>"""
    evidence_folder_id: NotRequired["aws_sdk_auditmanager.types.uuid.UUID"]
    """<p> The identifier for the folder that the evidence is stored in. </p>"""
    id: NotRequired["aws_sdk_auditmanager.types.uuid.UUID"]
    """<p> The identifier for the evidence. </p>"""
    assessment_report_selection: NotRequired["aws_sdk_auditmanager.types.string.String"]
    """<p> Specifies whether the evidence is included in the assessment report. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Evidence) -> dict:
    out: dict = {}
    if "data_source" in value:
        out["dataSource"] = value["data_source"]
    if "evidence_aws_account_id" in value:
        out["evidenceAwsAccountId"] = value["evidence_aws_account_id"]
    if "time" in value:
        import aws_sdk_auditmanager.types.timestamp

        out["time"] = aws_sdk_auditmanager.types.timestamp.serialize_json(value["time"])
    if "event_source" in value:
        out["eventSource"] = value["event_source"]
    if "event_name" in value:
        out["eventName"] = value["event_name"]
    if "evidence_by_type" in value:
        out["evidenceByType"] = value["evidence_by_type"]
    if "resources_included" in value:
        import aws_sdk_auditmanager.types.resources

        out["resourcesIncluded"] = aws_sdk_auditmanager.types.resources.serialize_json(
            value["resources_included"]
        )
    if "attributes" in value:
        import aws_sdk_auditmanager.types.evidence_attributes

        out["attributes"] = (
            aws_sdk_auditmanager.types.evidence_attributes.serialize_json(
                value["attributes"]
            )
        )
    if "iam_id" in value:
        out["iamId"] = value["iam_id"]
    if "compliance_check" in value:
        out["complianceCheck"] = value["compliance_check"]
    if "aws_organization" in value:
        out["awsOrganization"] = value["aws_organization"]
    if "aws_account_id" in value:
        out["awsAccountId"] = value["aws_account_id"]
    if "evidence_folder_id" in value:
        out["evidenceFolderId"] = value["evidence_folder_id"]
    if "id" in value:
        out["id"] = value["id"]
    if "assessment_report_selection" in value:
        out["assessmentReportSelection"] = value["assessment_report_selection"]
    return out


def deserialize_json(data: dict) -> Evidence:
    out: Evidence = {}  # type: ignore[typeddict-item]
    if "dataSource" in data:
        out["data_source"] = data["dataSource"]
    if "evidenceAwsAccountId" in data:
        out["evidence_aws_account_id"] = data["evidenceAwsAccountId"]
    if "time" in data:
        import aws_sdk_auditmanager.types.timestamp

        out["time"] = aws_sdk_auditmanager.types.timestamp.deserialize_json(
            data["time"]
        )
    if "eventSource" in data:
        out["event_source"] = data["eventSource"]
    if "eventName" in data:
        out["event_name"] = data["eventName"]
    if "evidenceByType" in data:
        out["evidence_by_type"] = data["evidenceByType"]
    if "resourcesIncluded" in data:
        import aws_sdk_auditmanager.types.resources

        out["resources_included"] = (
            aws_sdk_auditmanager.types.resources.deserialize_json(
                data["resourcesIncluded"]
            )
        )
    if "attributes" in data:
        import aws_sdk_auditmanager.types.evidence_attributes

        out["attributes"] = (
            aws_sdk_auditmanager.types.evidence_attributes.deserialize_json(
                data["attributes"]
            )
        )
    if "iamId" in data:
        out["iam_id"] = data["iamId"]
    if "complianceCheck" in data:
        out["compliance_check"] = data["complianceCheck"]
    if "awsOrganization" in data:
        out["aws_organization"] = data["awsOrganization"]
    if "awsAccountId" in data:
        out["aws_account_id"] = data["awsAccountId"]
    if "evidenceFolderId" in data:
        out["evidence_folder_id"] = data["evidenceFolderId"]
    if "id" in data:
        out["id"] = data["id"]
    if "assessmentReportSelection" in data:
        out["assessment_report_selection"] = data["assessmentReportSelection"]
    return out
