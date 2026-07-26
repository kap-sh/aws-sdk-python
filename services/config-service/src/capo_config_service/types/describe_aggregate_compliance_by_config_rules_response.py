"""Generated from Smithy shape ``com.amazonaws.configservice#DescribeAggregateComplianceByConfigRulesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.aggregate_compliance_by_config_rule_list
    import capo_config_service.types.next_token


class DescribeAggregateComplianceByConfigRulesResponse(TypedDict, closed=True):
    aggregate_compliance_by_config_rules: NotRequired[
        "capo_config_service.types.aggregate_compliance_by_config_rule_list.AggregateComplianceByConfigRuleList"
    ]
    """<p>Returns a list of AggregateComplianceByConfigRule object.</p>"""
    next_token: NotRequired["capo_config_service.types.next_token.NextToken"]
    """<p>The <code>nextToken</code> string returned on a previous page that you use to get the next page of results in a paginated response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: DescribeAggregateComplianceByConfigRulesResponse,
) -> dict:
    out: dict = {}
    if "aggregate_compliance_by_config_rules" in value:
        import capo_config_service.types.aggregate_compliance_by_config_rule_list

        out["AggregateComplianceByConfigRules"] = (
            capo_config_service.types.aggregate_compliance_by_config_rule_list.serialize_aws_json_1_1(
                value["aggregate_compliance_by_config_rules"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> DescribeAggregateComplianceByConfigRulesResponse:
    out: DescribeAggregateComplianceByConfigRulesResponse = {}  # type: ignore[typeddict-item]
    if "AggregateComplianceByConfigRules" in data:
        import capo_config_service.types.aggregate_compliance_by_config_rule_list

        out["aggregate_compliance_by_config_rules"] = (
            capo_config_service.types.aggregate_compliance_by_config_rule_list.deserialize_aws_json_1_1(
                data["AggregateComplianceByConfigRules"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
