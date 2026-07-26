"""Generated from Smithy shape ``com.amazonaws.configservice#ConfigRuleComplianceFilters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.account_id
    import capo_config_service.types.aws_region
    import capo_config_service.types.compliance_type
    import capo_config_service.types.config_rule_name


class ConfigRuleComplianceFilters(TypedDict, closed=True):
    config_rule_name: NotRequired[
        "capo_config_service.types.config_rule_name.ConfigRuleName"
    ]
    """<p>The name of the Config rule.</p>"""
    compliance_type: NotRequired[
        "capo_config_service.types.compliance_type.ComplianceType"
    ]
    """<p>The rule compliance status.</p> <p>For the <code>ConfigRuleComplianceFilters</code> data type, Config supports only <code>COMPLIANT</code> and <code>NON_COMPLIANT</code>. Config does not support the <code>NOT_APPLICABLE</code> and the <code>INSUFFICIENT_DATA</code> values.</p>"""
    account_id: NotRequired["capo_config_service.types.account_id.AccountId"]
    """<p>The 12-digit account ID of the source account. </p>"""
    aws_region: NotRequired["capo_config_service.types.aws_region.AwsRegion"]
    """<p>The source region where the data is aggregated. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConfigRuleComplianceFilters) -> dict:
    out: dict = {}
    if "config_rule_name" in value:
        out["ConfigRuleName"] = value["config_rule_name"]
    if "compliance_type" in value:
        import capo_config_service.types.compliance_type

        out["ComplianceType"] = (
            capo_config_service.types.compliance_type.serialize_aws_json_1_1(
                value["compliance_type"]
            )
        )
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    if "aws_region" in value:
        out["AwsRegion"] = value["aws_region"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ConfigRuleComplianceFilters:
    out: ConfigRuleComplianceFilters = {}  # type: ignore[typeddict-item]
    if "ConfigRuleName" in data:
        out["config_rule_name"] = data["ConfigRuleName"]
    if "ComplianceType" in data:
        import capo_config_service.types.compliance_type

        out["compliance_type"] = (
            capo_config_service.types.compliance_type.deserialize_aws_json_1_1(
                data["ComplianceType"]
            )
        )
    if "AccountId" in data:
        out["account_id"] = data["AccountId"]
    if "AwsRegion" in data:
        out["aws_region"] = data["AwsRegion"]
    return out
