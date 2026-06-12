"""Generated from Smithy shape ``com.amazonaws.costexplorer#GetCostAndUsageComparisonsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.comparison_metrics
    import aws_sdk_cost_explorer.types.cost_and_usage_comparisons
    import aws_sdk_cost_explorer.types.next_page_token


class GetCostAndUsageComparisonsResponse(TypedDict):
    cost_and_usage_comparisons: NotRequired[
        "aws_sdk_cost_explorer.types.cost_and_usage_comparisons.CostAndUsageComparisons"
    ]
    """<p>An array of comparison results showing cost and usage metrics between <code>BaselineTimePeriod</code> and <code>ComparisonTimePeriod</code>.</p>"""
    total_cost_and_usage: NotRequired[
        "aws_sdk_cost_explorer.types.comparison_metrics.ComparisonMetrics"
    ]
    """<p>A summary of the total cost and usage, comparing amounts between <code>BaselineTimePeriod</code> and <code>ComparisonTimePeriod</code> and their differences. This total represents the aggregate total across all paginated results, if the response spans multiple pages.</p>"""
    next_page_token: NotRequired[
        "aws_sdk_cost_explorer.types.next_page_token.NextPageToken"
    ]
    """<p>The token to retrieve the next set of paginated results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetCostAndUsageComparisonsResponse) -> dict:
    out: dict = {}
    if "cost_and_usage_comparisons" in value:
        import aws_sdk_cost_explorer.types.cost_and_usage_comparisons

        out["CostAndUsageComparisons"] = (
            aws_sdk_cost_explorer.types.cost_and_usage_comparisons.serialize_aws_json_1_1(
                value["cost_and_usage_comparisons"]
            )
        )
    if "total_cost_and_usage" in value:
        import aws_sdk_cost_explorer.types.comparison_metrics

        out["TotalCostAndUsage"] = (
            aws_sdk_cost_explorer.types.comparison_metrics.serialize_aws_json_1_1(
                value["total_cost_and_usage"]
            )
        )
    if "next_page_token" in value:
        out["NextPageToken"] = value["next_page_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetCostAndUsageComparisonsResponse:
    out: GetCostAndUsageComparisonsResponse = {}  # type: ignore[typeddict-item]
    if "CostAndUsageComparisons" in data:
        import aws_sdk_cost_explorer.types.cost_and_usage_comparisons

        out["cost_and_usage_comparisons"] = (
            aws_sdk_cost_explorer.types.cost_and_usage_comparisons.deserialize_aws_json_1_1(
                data["CostAndUsageComparisons"]
            )
        )
    if "TotalCostAndUsage" in data:
        import aws_sdk_cost_explorer.types.comparison_metrics

        out["total_cost_and_usage"] = (
            aws_sdk_cost_explorer.types.comparison_metrics.deserialize_aws_json_1_1(
                data["TotalCostAndUsage"]
            )
        )
    if "NextPageToken" in data:
        out["next_page_token"] = data["NextPageToken"]
    return out
