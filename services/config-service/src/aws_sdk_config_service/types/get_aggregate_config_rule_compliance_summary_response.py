"""Generated from Smithy shape ``com.amazonaws.configservice#GetAggregateConfigRuleComplianceSummaryResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_config_service.types.aggregate_compliance_count_list
    import aws_sdk_config_service.types.next_token
    import aws_sdk_config_service.types.string_with_char_limit256


class GetAggregateConfigRuleComplianceSummaryResponse(TypedDict, closed=True):
    group_by_key: NotRequired[
        "aws_sdk_config_service.types.string_with_char_limit256.StringWithCharLimit256"
    ]
    """<p>Groups the result based on ACCOUNT_ID or AWS_REGION.</p>"""
    aggregate_compliance_counts: NotRequired[
        "aws_sdk_config_service.types.aggregate_compliance_count_list.AggregateComplianceCountList"
    ]
    """<p>Returns a list of AggregateComplianceCounts object.</p>"""
    next_token: NotRequired["aws_sdk_config_service.types.next_token.NextToken"]
    """<p>The <code>nextToken</code> string returned on a previous page that you use to get the next page of results in a paginated response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: GetAggregateConfigRuleComplianceSummaryResponse,
) -> dict:
    out: dict = {}
    if "group_by_key" in value:
        out["GroupByKey"] = value["group_by_key"]
    if "aggregate_compliance_counts" in value:
        import aws_sdk_config_service.types.aggregate_compliance_count_list

        out["AggregateComplianceCounts"] = (
            aws_sdk_config_service.types.aggregate_compliance_count_list.serialize_aws_json_1_1(
                value["aggregate_compliance_counts"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> GetAggregateConfigRuleComplianceSummaryResponse:
    out: GetAggregateConfigRuleComplianceSummaryResponse = {}  # type: ignore[typeddict-item]
    if "GroupByKey" in data:
        out["group_by_key"] = data["GroupByKey"]
    if "AggregateComplianceCounts" in data:
        import aws_sdk_config_service.types.aggregate_compliance_count_list

        out["aggregate_compliance_counts"] = (
            aws_sdk_config_service.types.aggregate_compliance_count_list.deserialize_aws_json_1_1(
                data["AggregateComplianceCounts"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
