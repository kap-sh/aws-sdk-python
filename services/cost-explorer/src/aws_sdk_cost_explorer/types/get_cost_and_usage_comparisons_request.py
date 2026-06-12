"""Generated from Smithy shape ``com.amazonaws.costexplorer#GetCostAndUsageComparisonsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cost_explorer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.billing_view_arn
    import aws_sdk_cost_explorer.types.cost_and_usage_comparisons_max_results
    import aws_sdk_cost_explorer.types.date_interval
    import aws_sdk_cost_explorer.types.expression
    import aws_sdk_cost_explorer.types.group_definitions
    import aws_sdk_cost_explorer.types.metric_name
    import aws_sdk_cost_explorer.types.next_page_token


class GetCostAndUsageComparisonsRequest(TypedDict):
    billing_view_arn: NotRequired[
        "aws_sdk_cost_explorer.types.billing_view_arn.BillingViewArn"
    ]
    """<p>The Amazon Resource Name (ARN) that uniquely identifies a specific billing view. The ARN is used to specify which particular billing view you want to interact with or retrieve information from when making API calls related to Amazon Web Services Billing and Cost Management features. The BillingViewArn can be retrieved by calling the ListBillingViews API.</p>"""
    baseline_time_period: "aws_sdk_cost_explorer.types.date_interval.DateInterval"
    """<p>The reference time period for comparison. This time period serves as the baseline against which other cost and usage data will be compared. The interval must start and end on the first day of a month, with a duration of exactly one month.</p>"""
    comparison_time_period: "aws_sdk_cost_explorer.types.date_interval.DateInterval"
    """<p>The comparison time period for analysis. This time period's cost and usage data will be compared against the baseline time period. The interval must start and end on the first day of a month, with a duration of exactly one month.</p>"""
    metric_for_comparison: "aws_sdk_cost_explorer.types.metric_name.MetricName"
    """<p>The cost and usage metric to compare. Valid values are <code>AmortizedCost</code>, <code>BlendedCost</code>, <code>NetAmortizedCost</code>, <code>NetUnblendedCost</code>, <code>NormalizedUsageAmount</code>, <code>UnblendedCost</code>, and <code>UsageQuantity</code>.</p>"""
    filter: NotRequired["aws_sdk_cost_explorer.types.expression.Expression"]
    group_by: NotRequired[
        "aws_sdk_cost_explorer.types.group_definitions.GroupDefinitions"
    ]
    """<p>You can group results using the attributes <code>DIMENSION</code>, <code>TAG</code>, and <code>COST_CATEGORY</code>. </p>"""
    max_results: NotRequired[
        "aws_sdk_cost_explorer.types.cost_and_usage_comparisons_max_results.CostAndUsageComparisonsMaxResults"
    ]
    """<p>The maximum number of results that are returned for the request.</p>"""
    next_page_token: NotRequired[
        "aws_sdk_cost_explorer.types.next_page_token.NextPageToken"
    ]
    """<p>The token to retrieve the next set of paginated results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetCostAndUsageComparisonsRequest) -> dict:
    out: dict = {}
    if "billing_view_arn" in value:
        out["BillingViewArn"] = value["billing_view_arn"]
    import aws_sdk_cost_explorer.types.date_interval

    out["BaselineTimePeriod"] = (
        aws_sdk_cost_explorer.types.date_interval.serialize_aws_json_1_1(
            value["baseline_time_period"]
        )
    )
    import aws_sdk_cost_explorer.types.date_interval

    out["ComparisonTimePeriod"] = (
        aws_sdk_cost_explorer.types.date_interval.serialize_aws_json_1_1(
            value["comparison_time_period"]
        )
    )
    out["MetricForComparison"] = value["metric_for_comparison"]
    if "filter" in value:
        import aws_sdk_cost_explorer.types.expression

        out["Filter"] = aws_sdk_cost_explorer.types.expression.serialize_aws_json_1_1(
            value["filter"]
        )
    if "group_by" in value:
        import aws_sdk_cost_explorer.types.group_definitions

        out["GroupBy"] = (
            aws_sdk_cost_explorer.types.group_definitions.serialize_aws_json_1_1(
                value["group_by"]
            )
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_page_token" in value:
        out["NextPageToken"] = value["next_page_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetCostAndUsageComparisonsRequest:
    out: GetCostAndUsageComparisonsRequest = {}  # type: ignore[typeddict-item]
    if "BillingViewArn" in data:
        out["billing_view_arn"] = data["BillingViewArn"]
    if "BaselineTimePeriod" in data:
        import aws_sdk_cost_explorer.types.date_interval

        out["baseline_time_period"] = (
            aws_sdk_cost_explorer.types.date_interval.deserialize_aws_json_1_1(
                data["BaselineTimePeriod"]
            )
        )
    else:
        raise DeserializationError(
            "GetCostAndUsageComparisonsRequest.baseline_time_period required"
        )
    if "ComparisonTimePeriod" in data:
        import aws_sdk_cost_explorer.types.date_interval

        out["comparison_time_period"] = (
            aws_sdk_cost_explorer.types.date_interval.deserialize_aws_json_1_1(
                data["ComparisonTimePeriod"]
            )
        )
    else:
        raise DeserializationError(
            "GetCostAndUsageComparisonsRequest.comparison_time_period required"
        )
    if "MetricForComparison" in data:
        out["metric_for_comparison"] = data["MetricForComparison"]
    else:
        raise DeserializationError(
            "GetCostAndUsageComparisonsRequest.metric_for_comparison required"
        )
    if "Filter" in data:
        import aws_sdk_cost_explorer.types.expression

        out["filter"] = aws_sdk_cost_explorer.types.expression.deserialize_aws_json_1_1(
            data["Filter"]
        )
    if "GroupBy" in data:
        import aws_sdk_cost_explorer.types.group_definitions

        out["group_by"] = (
            aws_sdk_cost_explorer.types.group_definitions.deserialize_aws_json_1_1(
                data["GroupBy"]
            )
        )
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextPageToken" in data:
        out["next_page_token"] = data["NextPageToken"]
    return out
