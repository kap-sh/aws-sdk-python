"""Generated from Smithy shape ``com.amazonaws.ssm#ResourceComplianceSummaryItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.compliance_execution_summary
    import capo_ssm.types.compliance_resource_id
    import capo_ssm.types.compliance_resource_type
    import capo_ssm.types.compliance_severity
    import capo_ssm.types.compliance_status
    import capo_ssm.types.compliance_type_name
    import capo_ssm.types.compliant_summary
    import capo_ssm.types.non_compliant_summary


class ResourceComplianceSummaryItem(TypedDict, closed=True):
    compliance_type: NotRequired[
        "capo_ssm.types.compliance_type_name.ComplianceTypeName"
    ]
    """<p>The compliance type.</p>"""
    resource_type: NotRequired[
        "capo_ssm.types.compliance_resource_type.ComplianceResourceType"
    ]
    """<p>The resource type.</p>"""
    resource_id: NotRequired[
        "capo_ssm.types.compliance_resource_id.ComplianceResourceId"
    ]
    """<p>The resource ID.</p>"""
    status: NotRequired["capo_ssm.types.compliance_status.ComplianceStatus"]
    """<p>The compliance status for the resource.</p>"""
    overall_severity: NotRequired[
        "capo_ssm.types.compliance_severity.ComplianceSeverity"
    ]
    """<p>The highest severity item found for the resource. The resource is compliant for this item.</p>"""
    execution_summary: NotRequired[
        "capo_ssm.types.compliance_execution_summary.ComplianceExecutionSummary"
    ]
    """<p>Information about the execution.</p>"""
    compliant_summary: NotRequired["capo_ssm.types.compliant_summary.CompliantSummary"]
    """<p>A list of items that are compliant for the resource.</p>"""
    non_compliant_summary: NotRequired[
        "capo_ssm.types.non_compliant_summary.NonCompliantSummary"
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
        import capo_ssm.types.compliance_status

        out["Status"] = capo_ssm.types.compliance_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "overall_severity" in value:
        import capo_ssm.types.compliance_severity

        out["OverallSeverity"] = (
            capo_ssm.types.compliance_severity.serialize_aws_json_1_1(
                value["overall_severity"]
            )
        )
    if "execution_summary" in value:
        import capo_ssm.types.compliance_execution_summary

        out["ExecutionSummary"] = (
            capo_ssm.types.compliance_execution_summary.serialize_aws_json_1_1(
                value["execution_summary"]
            )
        )
    if "compliant_summary" in value:
        import capo_ssm.types.compliant_summary

        out["CompliantSummary"] = (
            capo_ssm.types.compliant_summary.serialize_aws_json_1_1(
                value["compliant_summary"]
            )
        )
    if "non_compliant_summary" in value:
        import capo_ssm.types.non_compliant_summary

        out["NonCompliantSummary"] = (
            capo_ssm.types.non_compliant_summary.serialize_aws_json_1_1(
                value["non_compliant_summary"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ResourceComplianceSummaryItem:
    out: ResourceComplianceSummaryItem = {}  # type: ignore[typeddict-item]
    if data.get("ComplianceType") is not None:
        out["compliance_type"] = data["ComplianceType"]
    if data.get("ResourceType") is not None:
        out["resource_type"] = data["ResourceType"]
    if data.get("ResourceId") is not None:
        out["resource_id"] = data["ResourceId"]
    if data.get("Status") is not None:
        import capo_ssm.types.compliance_status

        out["status"] = capo_ssm.types.compliance_status.deserialize_aws_json_1_1(
            data["Status"]
        )
    if data.get("OverallSeverity") is not None:
        import capo_ssm.types.compliance_severity

        out["overall_severity"] = (
            capo_ssm.types.compliance_severity.deserialize_aws_json_1_1(
                data["OverallSeverity"]
            )
        )
    if data.get("ExecutionSummary") is not None:
        import capo_ssm.types.compliance_execution_summary

        out["execution_summary"] = (
            capo_ssm.types.compliance_execution_summary.deserialize_aws_json_1_1(
                data["ExecutionSummary"]
            )
        )
    if data.get("CompliantSummary") is not None:
        import capo_ssm.types.compliant_summary

        out["compliant_summary"] = (
            capo_ssm.types.compliant_summary.deserialize_aws_json_1_1(
                data["CompliantSummary"]
            )
        )
    if data.get("NonCompliantSummary") is not None:
        import capo_ssm.types.non_compliant_summary

        out["non_compliant_summary"] = (
            capo_ssm.types.non_compliant_summary.deserialize_aws_json_1_1(
                data["NonCompliantSummary"]
            )
        )
    return out
