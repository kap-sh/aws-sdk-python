"""Generated from Smithy shape ``com.amazonaws.ssm#ResourceComplianceSummaryItem``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ssm.types.compliance_execution_summary
    import aws_sdk_ssm.types.compliance_resource_id
    import aws_sdk_ssm.types.compliance_resource_type
    import aws_sdk_ssm.types.compliance_severity
    import aws_sdk_ssm.types.compliance_status
    import aws_sdk_ssm.types.compliance_type_name
    import aws_sdk_ssm.types.compliant_summary
    import aws_sdk_ssm.types.non_compliant_summary


class ResourceComplianceSummaryItem(TypedDict):
    compliance_type: NotRequired[
        "aws_sdk_ssm.types.compliance_type_name.ComplianceTypeName"
    ]
    """<p>The compliance type.</p>"""
    resource_type: NotRequired[
        "aws_sdk_ssm.types.compliance_resource_type.ComplianceResourceType"
    ]
    """<p>The resource type.</p>"""
    resource_id: NotRequired[
        "aws_sdk_ssm.types.compliance_resource_id.ComplianceResourceId"
    ]
    """<p>The resource ID.</p>"""
    status: NotRequired["aws_sdk_ssm.types.compliance_status.ComplianceStatus"]
    """<p>The compliance status for the resource.</p>"""
    overall_severity: NotRequired[
        "aws_sdk_ssm.types.compliance_severity.ComplianceSeverity"
    ]
    """<p>The highest severity item found for the resource. The resource is compliant for this item.</p>"""
    execution_summary: NotRequired[
        "aws_sdk_ssm.types.compliance_execution_summary.ComplianceExecutionSummary"
    ]
    """<p>Information about the execution.</p>"""
    compliant_summary: NotRequired[
        "aws_sdk_ssm.types.compliant_summary.CompliantSummary"
    ]
    """<p>A list of items that are compliant for the resource.</p>"""
    non_compliant_summary: NotRequired[
        "aws_sdk_ssm.types.non_compliant_summary.NonCompliantSummary"
    ]
    """<p>A list of items that aren't compliant for the resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceComplianceSummaryItem) -> dict:
    out: dict = {}
    if "compliance_type" in value:
        out["ComplianceType"] = value["compliance_type"]
    if "resource_type" in value:
        out["ResourceType"] = value["resource_type"]
    if "resource_id" in value:
        out["ResourceId"] = value["resource_id"]
    if "status" in value:
        import aws_sdk_ssm.types.compliance_status

        out["Status"] = aws_sdk_ssm.types.compliance_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "overall_severity" in value:
        import aws_sdk_ssm.types.compliance_severity

        out["OverallSeverity"] = (
            aws_sdk_ssm.types.compliance_severity.serialize_aws_json_1_1(
                value["overall_severity"]
            )
        )
    if "execution_summary" in value:
        import aws_sdk_ssm.types.compliance_execution_summary

        out["ExecutionSummary"] = (
            aws_sdk_ssm.types.compliance_execution_summary.serialize_aws_json_1_1(
                value["execution_summary"]
            )
        )
    if "compliant_summary" in value:
        import aws_sdk_ssm.types.compliant_summary

        out["CompliantSummary"] = (
            aws_sdk_ssm.types.compliant_summary.serialize_aws_json_1_1(
                value["compliant_summary"]
            )
        )
    if "non_compliant_summary" in value:
        import aws_sdk_ssm.types.non_compliant_summary

        out["NonCompliantSummary"] = (
            aws_sdk_ssm.types.non_compliant_summary.serialize_aws_json_1_1(
                value["non_compliant_summary"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ResourceComplianceSummaryItem:
    out: ResourceComplianceSummaryItem = {}  # type: ignore[typeddict-item]
    if "ComplianceType" in data:
        out["compliance_type"] = data["ComplianceType"]
    if "ResourceType" in data:
        out["resource_type"] = data["ResourceType"]
    if "ResourceId" in data:
        out["resource_id"] = data["ResourceId"]
    if "Status" in data:
        import aws_sdk_ssm.types.compliance_status

        out["status"] = aws_sdk_ssm.types.compliance_status.deserialize_aws_json_1_1(
            data["Status"]
        )
    if "OverallSeverity" in data:
        import aws_sdk_ssm.types.compliance_severity

        out["overall_severity"] = (
            aws_sdk_ssm.types.compliance_severity.deserialize_aws_json_1_1(
                data["OverallSeverity"]
            )
        )
    if "ExecutionSummary" in data:
        import aws_sdk_ssm.types.compliance_execution_summary

        out["execution_summary"] = (
            aws_sdk_ssm.types.compliance_execution_summary.deserialize_aws_json_1_1(
                data["ExecutionSummary"]
            )
        )
    if "CompliantSummary" in data:
        import aws_sdk_ssm.types.compliant_summary

        out["compliant_summary"] = (
            aws_sdk_ssm.types.compliant_summary.deserialize_aws_json_1_1(
                data["CompliantSummary"]
            )
        )
    if "NonCompliantSummary" in data:
        import aws_sdk_ssm.types.non_compliant_summary

        out["non_compliant_summary"] = (
            aws_sdk_ssm.types.non_compliant_summary.deserialize_aws_json_1_1(
                data["NonCompliantSummary"]
            )
        )
    return out
