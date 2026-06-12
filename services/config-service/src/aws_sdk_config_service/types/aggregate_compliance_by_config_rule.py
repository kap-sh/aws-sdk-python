"""Generated from Smithy shape ``com.amazonaws.configservice#AggregateComplianceByConfigRule``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_config_service.types.account_id
    import aws_sdk_config_service.types.aws_region
    import aws_sdk_config_service.types.compliance
    import aws_sdk_config_service.types.config_rule_name


class AggregateComplianceByConfigRule(TypedDict):
    config_rule_name: NotRequired[
        "aws_sdk_config_service.types.config_rule_name.ConfigRuleName"
    ]
    """<p>The name of the Config rule.</p>"""
    compliance: NotRequired["aws_sdk_config_service.types.compliance.Compliance"]
    """<p>Indicates whether an Amazon Web Services resource or Config rule is compliant and provides the number of contributors that affect the compliance.</p>"""
    account_id: NotRequired["aws_sdk_config_service.types.account_id.AccountId"]
    """<p>The 12-digit account ID of the source account.</p>"""
    aws_region: NotRequired["aws_sdk_config_service.types.aws_region.AwsRegion"]
    """<p>The source region from where the data is aggregated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AggregateComplianceByConfigRule) -> dict:
    out: dict = {}
    if "config_rule_name" in value:
        out["ConfigRuleName"] = value["config_rule_name"]
    if "compliance" in value:
        import aws_sdk_config_service.types.compliance

        out["Compliance"] = (
            aws_sdk_config_service.types.compliance.serialize_aws_json_1_1(
                value["compliance"]
            )
        )
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    if "aws_region" in value:
        out["AwsRegion"] = value["aws_region"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AggregateComplianceByConfigRule:
    out: AggregateComplianceByConfigRule = {}  # type: ignore[typeddict-item]
    if "ConfigRuleName" in data:
        out["config_rule_name"] = data["ConfigRuleName"]
    if "Compliance" in data:
        import aws_sdk_config_service.types.compliance

        out["compliance"] = (
            aws_sdk_config_service.types.compliance.deserialize_aws_json_1_1(
                data["Compliance"]
            )
        )
    if "AccountId" in data:
        out["account_id"] = data["AccountId"]
    if "AwsRegion" in data:
        out["aws_region"] = data["AwsRegion"]
    return out
