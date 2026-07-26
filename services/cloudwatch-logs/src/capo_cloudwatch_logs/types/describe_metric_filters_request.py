"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#DescribeMetricFiltersRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.describe_limit
    import capo_cloudwatch_logs.types.filter_name
    import capo_cloudwatch_logs.types.log_group_name
    import capo_cloudwatch_logs.types.metric_name
    import capo_cloudwatch_logs.types.metric_namespace
    import capo_cloudwatch_logs.types.next_token


class DescribeMetricFiltersRequest(TypedDict, closed=True):
    log_group_name: NotRequired[
        "capo_cloudwatch_logs.types.log_group_name.LogGroupName"
    ]
    """<p>The name of the log group.</p>"""
    filter_name_prefix: NotRequired["capo_cloudwatch_logs.types.filter_name.FilterName"]
    """<p>The prefix to match. CloudWatch Logs uses the value that you set here only if you also include the <code>logGroupName</code> parameter in your request.</p>"""
    next_token: NotRequired["capo_cloudwatch_logs.types.next_token.NextToken"]
    """<p>The token for the next set of items to return. (You received this token from a previous call.)</p>"""
    limit: NotRequired["capo_cloudwatch_logs.types.describe_limit.DescribeLimit"]
    """<p>The maximum number of items returned. If you don't specify a value, the default is up to 50 items.</p>"""
    metric_name: NotRequired["capo_cloudwatch_logs.types.metric_name.MetricName"]
    """<p>Filters results to include only those with the specified metric name. If you include this parameter in your request, you must also include the <code>metricNamespace</code> parameter.</p>"""
    metric_namespace: NotRequired[
        "capo_cloudwatch_logs.types.metric_namespace.MetricNamespace"
    ]
    """<p>Filters results to include only those in the specified namespace. If you include this parameter in your request, you must also include the <code>metricName</code> parameter.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeMetricFiltersRequest) -> dict:
    out: dict = {}
    if "log_group_name" in value:
        out["logGroupName"] = value["log_group_name"]
    if "filter_name_prefix" in value:
        out["filterNamePrefix"] = value["filter_name_prefix"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "limit" in value:
        out["limit"] = value["limit"]
    if "metric_name" in value:
        out["metricName"] = value["metric_name"]
    if "metric_namespace" in value:
        out["metricNamespace"] = value["metric_namespace"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeMetricFiltersRequest:
    out: DescribeMetricFiltersRequest = {}  # type: ignore[typeddict-item]
    if "logGroupName" in data:
        out["log_group_name"] = data["logGroupName"]
    if "filterNamePrefix" in data:
        out["filter_name_prefix"] = data["filterNamePrefix"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "limit" in data:
        out["limit"] = data["limit"]
    if "metricName" in data:
        out["metric_name"] = data["metricName"]
    if "metricNamespace" in data:
        out["metric_namespace"] = data["metricNamespace"]
    return out
