"""Generated from Smithy shape ``com.amazonaws.ec2#MetricValue``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.double
    import aws_sdk_ec2.types.metric


class MetricValue(TypedDict):
    metric: NotRequired["aws_sdk_ec2.types.metric.Metric"]
    """<p> The name of the metric. </p>"""
    value: NotRequired["aws_sdk_ec2.types.double.Double"]
    """<p> The numerical value of the metric for the specified statistic and time period. </p>"""
