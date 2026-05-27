"""Generated from Smithy shape ``com.amazonaws.ec2#GetCapacityManagerMetricDimensionsRequest``."""

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


class GetCapacityManagerMetricDimensionsRequest(TypedDict):
    group_by: NotRequired["aws_sdk_ec2.types.group_by_set.GroupBySet"]
    """<p> The dimensions to group by when retrieving available dimension values. This determines which dimension combinations are returned. Required parameter. </p>"""
    filter_by: NotRequired[
        "aws_sdk_ec2.types.capacity_manager_condition_set.CapacityManagerConditionSet"
    ]
    """<p> Conditions to filter which dimension values are returned. Each filter specifies a dimension, comparison operator, and values to match against. </p>"""
    start_time: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p> The start time for the dimension query, in ISO 8601 format. Only dimensions with data in this time range will be returned. </p>"""
    end_time: NotRequired["aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"]
    """<p> The end time for the dimension query, in ISO 8601 format. Only dimensions with data in this time range will be returned. </p>"""
    metric_names: NotRequired["aws_sdk_ec2.types.metric_set.MetricSet"]
    """<p> The metric names to use as an additional filter when retrieving dimensions. Only dimensions that have data for these metrics will be returned. Required parameter with maximum size of 1 for v1. </p>"""
    max_results: NotRequired["aws_sdk_ec2.types.max_results.MaxResults"]
    """<p> The maximum number of dimension combinations to return. Valid range is 1 to 1000. Use with NextToken for pagination. </p>"""
    next_token: NotRequired["aws_sdk_ec2.types.next_token.NextToken"]
    """<p> The token for the next page of results. Use this value in a subsequent call to retrieve additional dimension values. </p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p> Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>. </p>"""
