"""Generated from Smithy shape ``com.amazonaws.ec2#GetCapacityManagerMetricDataResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.metric_data_result_set
    import aws_sdk_ec2.types.next_token


class GetCapacityManagerMetricDataResult(TypedDict):
    metric_data_results: NotRequired[
        "aws_sdk_ec2.types.metric_data_result_set.MetricDataResultSet"
    ]
    """<p> The metric data points returned by the query. Each result contains dimension values, timestamp, and metric values with their associated statistics. </p>"""
    next_token: NotRequired["aws_sdk_ec2.types.next_token.NextToken"]
    """<p> The token to use to retrieve the next page of results. This value is null when there are no more results to return. </p>"""
