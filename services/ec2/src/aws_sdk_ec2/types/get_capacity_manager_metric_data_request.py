"""Generated from Smithy shape ``com.amazonaws.ec2#GetCapacityManagerMetricDataRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.capacity_manager_condition_set
    import aws_sdk_ec2.types.group_by_set
    import aws_sdk_ec2.types.max_results
    import aws_sdk_ec2.types.metric_set
    import aws_sdk_ec2.types.millisecond_date_time
    import aws_sdk_ec2.types.next_token
    import aws_sdk_ec2.types.period


class GetCapacityManagerMetricDataRequest(TypedDict):
    metric_names: NotRequired["aws_sdk_ec2.types.metric_set.MetricSet"]
    """<p> The names of the metrics to retrieve. Maximum of 10 metrics per request. </p>"""
    start_time: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p> The start time for the metric data query, in ISO 8601 format. The time range (end time - start time) must be a multiple of the specified period. </p>"""
    end_time: NotRequired["aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"]
    """<p> The end time for the metric data query, in ISO 8601 format. If the end time is beyond the latest ingested data, it will be automatically adjusted to the latest available data point. </p>"""
    period: NotRequired["aws_sdk_ec2.types.period.Period"]
    """<p> The granularity, in seconds, of the returned data points. </p>"""
    group_by: NotRequired["aws_sdk_ec2.types.group_by_set.GroupBySet"]
    """<p> The dimensions by which to group the metric data. This determines how the data is aggregated and returned. </p>"""
    filter_by: NotRequired[
        "aws_sdk_ec2.types.capacity_manager_condition_set.CapacityManagerConditionSet"
    ]
    """<p> Conditions to filter the metric data. Each filter specifies a dimension, comparison operator ('equals', 'in'), and values to match against. </p>"""
    max_results: NotRequired["aws_sdk_ec2.types.max_results.MaxResults"]
    """<p> The maximum number of data points to return. Valid range is 1 to 100,000. Use with NextToken for pagination of large result sets. </p>"""
    next_token: NotRequired["aws_sdk_ec2.types.next_token.NextToken"]
    """<p> The token for the next page of results. Use this value in a subsequent call to retrieve additional data points. </p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p> Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>. </p>"""
