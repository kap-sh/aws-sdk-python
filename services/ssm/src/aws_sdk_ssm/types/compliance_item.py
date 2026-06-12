"""Generated from Smithy shape ``com.amazonaws.ssm#ComplianceItem``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ssm.types.compliance_execution_summary
    import aws_sdk_ssm.types.compliance_item_details
    import aws_sdk_ssm.types.compliance_item_id
    import aws_sdk_ssm.types.compliance_item_title
    import aws_sdk_ssm.types.compliance_resource_id
    import aws_sdk_ssm.types.compliance_resource_type
    import aws_sdk_ssm.types.compliance_severity
    import aws_sdk_ssm.types.compliance_status
    import aws_sdk_ssm.types.compliance_type_name


class ComplianceItem(TypedDict):
    compliance_type: NotRequired[
        "aws_sdk_ssm.types.compliance_type_name.ComplianceTypeName"
    ]
    """<p>The compliance type. For example, Association (for a State Manager association), Patch, or Custom:<code>string</code> are all valid compliance types.</p>"""
    resource_type: NotRequired[
        "aws_sdk_ssm.types.compliance_resource_type.ComplianceResourceType"
    ]
    """<p>The type of resource. <code>ManagedInstance</code> is currently the only supported resource type.</p>"""
    resource_id: NotRequired[
        "aws_sdk_ssm.types.compliance_resource_id.ComplianceResourceId"
    ]
    """<p>An ID for the resource. For a managed node, this is the node ID.</p>"""
    id: NotRequired["aws_sdk_ssm.types.compliance_item_id.ComplianceItemId"]
    """<p>An ID for the compliance item. For example, if the compliance item is a Windows patch, the ID could be the number of the KB article; for example: KB4010320.</p>"""
    title: NotRequired["aws_sdk_ssm.types.compliance_item_title.ComplianceItemTitle"]
    """<p>A title for the compliance item. For example, if the compliance item is a Windows patch, the title could be the title of the KB article for the patch; for example: Security Update for Active Directory Federation Services.</p>"""
    status: NotRequired["aws_sdk_ssm.types.compliance_status.ComplianceStatus"]
    """<p>The status of the compliance item. An item is either COMPLIANT, NON_COMPLIANT, or an empty string (for Windows patches that aren't applicable).</p>"""
    severity: NotRequired["aws_sdk_ssm.types.compliance_severity.ComplianceSeverity"]
    """<p>The severity of the compliance status. Severity can be one of the following: Critical, High, Medium, Low, Informational, Unspecified.</p>"""
    execution_summary: NotRequired[
        "aws_sdk_ssm.types.compliance_execution_summary.ComplianceExecutionSummary"
    ]
    """<p>A summary for the compliance item. The summary includes an execution ID, the execution type (for example, command), and the execution time.</p> <important> <p>For State Manager associations, the <code>ExecutionTime</code> value represents when the compliance status was captured and aggregated by the Systems Manager service, not necessarily when the underlying association was executed on the managed node. State Manager updates compliance status for all associations on an instance whenever any association executes, which means multiple associations may show the same execution time even if they were executed at different times.</p> </important>"""
    details: NotRequired[
        "aws_sdk_ssm.types.compliance_item_details.ComplianceItemDetails"
    ]
    """<p>A \"Key\": \"Value\" tag combination for the compliance item.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ComplianceItem) -> dict:
    out: dict = {}
    if "compliance_type" in value:
        out["ComplianceType"] = value["compliance_type"]
    if "resource_type" in value:
        out["ResourceType"] = value["resource_type"]
    if "resource_id" in value:
        out["ResourceId"] = value["resource_id"]
    if "id" in value:
        out["Id"] = value["id"]
    if "title" in value:
        out["Title"] = value["title"]
    if "status" in value:
        import aws_sdk_ssm.types.compliance_status

        out["Status"] = aws_sdk_ssm.types.compliance_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "severity" in value:
        import aws_sdk_ssm.types.compliance_severity

        out["Severity"] = aws_sdk_ssm.types.compliance_severity.serialize_aws_json_1_1(
            value["severity"]
        )
    if "execution_summary" in value:
        import aws_sdk_ssm.types.compliance_execution_summary

        out["ExecutionSummary"] = (
            aws_sdk_ssm.types.compliance_execution_summary.serialize_aws_json_1_1(
                value["execution_summary"]
            )
        )
    if "details" in value:
        import aws_sdk_ssm.types.compliance_item_details

        out["Details"] = (
            aws_sdk_ssm.types.compliance_item_details.serialize_aws_json_1_1(
                value["details"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ComplianceItem:
    out: ComplianceItem = {}  # type: ignore[typeddict-item]
    if "ComplianceType" in data:
        out["compliance_type"] = data["ComplianceType"]
    if "ResourceType" in data:
        out["resource_type"] = data["ResourceType"]
    if "ResourceId" in data:
        out["resource_id"] = data["ResourceId"]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Title" in data:
        out["title"] = data["Title"]
    if "Status" in data:
        import aws_sdk_ssm.types.compliance_status

        out["status"] = aws_sdk_ssm.types.compliance_status.deserialize_aws_json_1_1(
            data["Status"]
        )
    if "Severity" in data:
        import aws_sdk_ssm.types.compliance_severity

        out["severity"] = (
            aws_sdk_ssm.types.compliance_severity.deserialize_aws_json_1_1(
                data["Severity"]
            )
        )
    if "ExecutionSummary" in data:
        import aws_sdk_ssm.types.compliance_execution_summary

        out["execution_summary"] = (
            aws_sdk_ssm.types.compliance_execution_summary.deserialize_aws_json_1_1(
                data["ExecutionSummary"]
            )
        )
    if "Details" in data:
        import aws_sdk_ssm.types.compliance_item_details

        out["details"] = (
            aws_sdk_ssm.types.compliance_item_details.deserialize_aws_json_1_1(
                data["Details"]
            )
        )
    return out
