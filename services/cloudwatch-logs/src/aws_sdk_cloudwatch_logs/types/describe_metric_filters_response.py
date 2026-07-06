"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#DescribeMetricFiltersResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.metric_filters
    import aws_sdk_cloudwatch_logs.types.next_token


class DescribeMetricFiltersResponse(TypedDict, closed=True):
    metric_filters: NotRequired[
        "aws_sdk_cloudwatch_logs.types.metric_filters.MetricFilters"
    ]
    """<p>The metric filters.</p>"""
    next_token: NotRequired["aws_sdk_cloudwatch_logs.types.next_token.NextToken"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeMetricFiltersResponse) -> dict:
    out: dict = {}
    if "metric_filters" in value:
        import aws_sdk_cloudwatch_logs.types.metric_filters

        out["metricFilters"] = (
            aws_sdk_cloudwatch_logs.types.metric_filters.serialize_aws_json_1_1(
                value["metric_filters"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeMetricFiltersResponse:
    out: DescribeMetricFiltersResponse = {}  # type: ignore[typeddict-item]
    if "metricFilters" in data:
        import aws_sdk_cloudwatch_logs.types.metric_filters

        out["metric_filters"] = (
            aws_sdk_cloudwatch_logs.types.metric_filters.deserialize_aws_json_1_1(
                data["metricFilters"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
