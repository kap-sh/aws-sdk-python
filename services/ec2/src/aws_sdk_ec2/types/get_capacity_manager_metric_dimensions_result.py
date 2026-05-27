"""Generated from Smithy shape ``com.amazonaws.ec2#GetCapacityManagerMetricDimensionsResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.metric_dimension_result_set
    import aws_sdk_ec2.types.next_token


class GetCapacityManagerMetricDimensionsResult(TypedDict):
    metric_dimension_results: NotRequired[
        "aws_sdk_ec2.types.metric_dimension_result_set.MetricDimensionResultSet"
    ]
    """<p> The available dimension combinations that have data within the specified time range and filters. </p>"""
    next_token: NotRequired["aws_sdk_ec2.types.next_token.NextToken"]
    """<p> The token to use to retrieve the next page of results. This value is null when there are no more results to return. </p>"""
