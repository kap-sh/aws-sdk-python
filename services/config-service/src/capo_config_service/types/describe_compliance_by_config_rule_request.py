"""Generated from Smithy shape ``com.amazonaws.configservice#DescribeComplianceByConfigRuleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.compliance_types
    import capo_config_service.types.config_rule_names
    import capo_config_service.types.string


class DescribeComplianceByConfigRuleRequest(TypedDict, closed=True):
    config_rule_names: NotRequired[
        "capo_config_service.types.config_rule_names.ConfigRuleNames"
    ]
    """<p>Specify one or more Config rule names to filter the results by rule.</p>"""
    compliance_types: NotRequired[
        "capo_config_service.types.compliance_types.ComplianceTypes"
    ]
    """<p>Filters the results by compliance.</p>"""
    next_token: NotRequired["capo_config_service.types.string.String"]
    """<p>The <code>nextToken</code> string returned on a previous page that you use to get the next page of results in a paginated response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeComplianceByConfigRuleRequest) -> dict:
    out: dict = {}
    if "config_rule_names" in value:
        import capo_config_service.types.config_rule_names

        out["ConfigRuleNames"] = (
            capo_config_service.types.config_rule_names.serialize_aws_json_1_1(
                value["config_rule_names"]
            )
        )
    if "compliance_types" in value:
        import capo_config_service.types.compliance_types

        out["ComplianceTypes"] = (
            capo_config_service.types.compliance_types.serialize_aws_json_1_1(
                value["compliance_types"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeComplianceByConfigRuleRequest:
    out: DescribeComplianceByConfigRuleRequest = {}  # type: ignore[typeddict-item]
    if "ConfigRuleNames" in data:
        import capo_config_service.types.config_rule_names

        out["config_rule_names"] = (
            capo_config_service.types.config_rule_names.deserialize_aws_json_1_1(
                data["ConfigRuleNames"]
            )
        )
    if "ComplianceTypes" in data:
        import capo_config_service.types.compliance_types

        out["compliance_types"] = (
            capo_config_service.types.compliance_types.deserialize_aws_json_1_1(
                data["ComplianceTypes"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
