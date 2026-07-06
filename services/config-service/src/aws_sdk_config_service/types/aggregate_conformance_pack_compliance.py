"""Generated from Smithy shape ``com.amazonaws.configservice#AggregateConformancePackCompliance``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_config_service.types.conformance_pack_compliance_type
    import aws_sdk_config_service.types.integer


class AggregateConformancePackCompliance(TypedDict, closed=True):
    compliance_type: NotRequired[
        "aws_sdk_config_service.types.conformance_pack_compliance_type.ConformancePackComplianceType"
    ]
    """<p>The compliance status of the conformance pack.</p>"""
    compliant_rule_count: "aws_sdk_config_service.types.integer.Integer"
    """<p>The number of compliant Config Rules.</p>"""
    non_compliant_rule_count: "aws_sdk_config_service.types.integer.Integer"
    """<p>The number of noncompliant Config Rules.</p>"""
    total_rule_count: "aws_sdk_config_service.types.integer.Integer"
    """<p>Total number of compliant rules, noncompliant rules, and the rules that do not have any applicable resources to evaluate upon resulting in insufficient data.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AggregateConformancePackCompliance) -> dict:
    out: dict = {}
    if "compliance_type" in value:
        import aws_sdk_config_service.types.conformance_pack_compliance_type

        out["ComplianceType"] = (
            aws_sdk_config_service.types.conformance_pack_compliance_type.serialize_aws_json_1_1(
                value["compliance_type"]
            )
        )
    out["CompliantRuleCount"] = value.get("compliant_rule_count", 0)
    out["NonCompliantRuleCount"] = value.get("non_compliant_rule_count", 0)
    out["TotalRuleCount"] = value.get("total_rule_count", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> AggregateConformancePackCompliance:
    out: AggregateConformancePackCompliance = {}  # type: ignore[typeddict-item]
    if "ComplianceType" in data:
        import aws_sdk_config_service.types.conformance_pack_compliance_type

        out["compliance_type"] = (
            aws_sdk_config_service.types.conformance_pack_compliance_type.deserialize_aws_json_1_1(
                data["ComplianceType"]
            )
        )
    if "CompliantRuleCount" in data:
        out["compliant_rule_count"] = data["CompliantRuleCount"]
    else:
        out["compliant_rule_count"] = 0
    if "NonCompliantRuleCount" in data:
        out["non_compliant_rule_count"] = data["NonCompliantRuleCount"]
    else:
        out["non_compliant_rule_count"] = 0
    if "TotalRuleCount" in data:
        out["total_rule_count"] = data["TotalRuleCount"]
    else:
        out["total_rule_count"] = 0
    return out
