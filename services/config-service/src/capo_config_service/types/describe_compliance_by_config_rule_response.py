"""Generated from Smithy shape ``com.amazonaws.configservice#DescribeComplianceByConfigRuleResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.compliance_by_config_rules
    import capo_config_service.types.string


class DescribeComplianceByConfigRuleResponse(TypedDict, closed=True):
    compliance_by_config_rules: NotRequired[
        "capo_config_service.types.compliance_by_config_rules.ComplianceByConfigRules"
    ]
    """<p>Indicates whether each of the specified Config rules is compliant.</p>"""
    next_token: NotRequired["capo_config_service.types.string.String"]
    """<p>The string that you use in a subsequent request to get the next page of results in a paginated response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeComplianceByConfigRuleResponse) -> dict:
    out: dict = {}
    if "compliance_by_config_rules" in value:
        import capo_config_service.types.compliance_by_config_rules

        out["ComplianceByConfigRules"] = (
            capo_config_service.types.compliance_by_config_rules.serialize_aws_json_1_1(
                value["compliance_by_config_rules"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeComplianceByConfigRuleResponse:
    out: DescribeComplianceByConfigRuleResponse = {}  # type: ignore[typeddict-item]
    if "ComplianceByConfigRules" in data:
        import capo_config_service.types.compliance_by_config_rules

        out["compliance_by_config_rules"] = (
            capo_config_service.types.compliance_by_config_rules.deserialize_aws_json_1_1(
                data["ComplianceByConfigRules"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
