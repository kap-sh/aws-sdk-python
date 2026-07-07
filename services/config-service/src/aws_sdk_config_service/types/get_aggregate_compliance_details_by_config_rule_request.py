"""Generated from Smithy shape ``com.amazonaws.configservice#GetAggregateComplianceDetailsByConfigRuleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_config_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_config_service.types.account_id
    import aws_sdk_config_service.types.aws_region
    import aws_sdk_config_service.types.compliance_type
    import aws_sdk_config_service.types.config_rule_name
    import aws_sdk_config_service.types.configuration_aggregator_name
    import aws_sdk_config_service.types.limit
    import aws_sdk_config_service.types.next_token


class GetAggregateComplianceDetailsByConfigRuleRequest(TypedDict, closed=True):
    configuration_aggregator_name: "aws_sdk_config_service.types.configuration_aggregator_name.ConfigurationAggregatorName"
    """<p>The name of the configuration aggregator.</p>"""
    config_rule_name: "aws_sdk_config_service.types.config_rule_name.ConfigRuleName"
    """<p>The name of the Config rule for which you want compliance information.</p>"""
    account_id: "aws_sdk_config_service.types.account_id.AccountId"
    """<p>The 12-digit account ID of the source account.</p>"""
    aws_region: "aws_sdk_config_service.types.aws_region.AwsRegion"
    """<p>The source region from where the data is aggregated.</p>"""
    compliance_type: NotRequired[
        "aws_sdk_config_service.types.compliance_type.ComplianceType"
    ]
    """<p>The resource compliance status.</p> <note> <p>For the <code>GetAggregateComplianceDetailsByConfigRuleRequest</code> data type, Config supports only the <code>COMPLIANT</code> and <code>NON_COMPLIANT</code>. Config does not support the <code>NOT_APPLICABLE</code> and <code>INSUFFICIENT_DATA</code> values.</p> </note>"""
    limit: "aws_sdk_config_service.types.limit.Limit"
    """<p>The maximum number of evaluation results returned on each page. The default is 50. You cannot specify a number greater than 100. If you specify 0, Config uses the default.</p>"""
    next_token: NotRequired["aws_sdk_config_service.types.next_token.NextToken"]
    """<p>The <code>nextToken</code> string returned on a previous page that you use to get the next page of results in a paginated response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: GetAggregateComplianceDetailsByConfigRuleRequest,
) -> dict:
    out: dict = {}
    out["ConfigurationAggregatorName"] = value["configuration_aggregator_name"]
    out["ConfigRuleName"] = value["config_rule_name"]
    out["AccountId"] = value["account_id"]
    out["AwsRegion"] = value["aws_region"]
    if "compliance_type" in value:
        import aws_sdk_config_service.types.compliance_type

        out["ComplianceType"] = (
            aws_sdk_config_service.types.compliance_type.serialize_aws_json_1_1(
                value["compliance_type"]
            )
        )
    out["Limit"] = value.get("limit", 0)
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> GetAggregateComplianceDetailsByConfigRuleRequest:
    out: GetAggregateComplianceDetailsByConfigRuleRequest = {}  # type: ignore[typeddict-item]
    if "ConfigurationAggregatorName" in data:
        out["configuration_aggregator_name"] = data["ConfigurationAggregatorName"]
    else:
        raise DeserializationError(
            "GetAggregateComplianceDetailsByConfigRuleRequest.configuration_aggregator_name required"
        )
    if "ConfigRuleName" in data:
        out["config_rule_name"] = data["ConfigRuleName"]
    else:
        raise DeserializationError(
            "GetAggregateComplianceDetailsByConfigRuleRequest.config_rule_name required"
        )
    if "AccountId" in data:
        out["account_id"] = data["AccountId"]
    else:
        raise DeserializationError(
            "GetAggregateComplianceDetailsByConfigRuleRequest.account_id required"
        )
    if "AwsRegion" in data:
        out["aws_region"] = data["AwsRegion"]
    else:
        raise DeserializationError(
            "GetAggregateComplianceDetailsByConfigRuleRequest.aws_region required"
        )
    if "ComplianceType" in data:
        import aws_sdk_config_service.types.compliance_type

        out["compliance_type"] = (
            aws_sdk_config_service.types.compliance_type.deserialize_aws_json_1_1(
                data["ComplianceType"]
            )
        )
    if "Limit" in data:
        out["limit"] = data["Limit"]
    else:
        out["limit"] = 0
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
