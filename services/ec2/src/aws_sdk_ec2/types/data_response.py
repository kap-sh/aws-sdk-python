"""Generated from Smithy shape ``com.amazonaws.ec2#DataResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.metric_points
    import aws_sdk_ec2.types.metric_type
    import aws_sdk_ec2.types.period_type
    import aws_sdk_ec2.types.statistic_type
    import aws_sdk_ec2.types.string


class DataResponse(TypedDict):
    id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID passed in the <code>DataQuery</code>.</p>"""
    source: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Region or Availability Zone that's the source for the data query. For example, <code>us-east-1</code>.</p>"""
    destination: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Region or Availability Zone that's the destination for the data query. For example, <code>eu-west-1</code>.</p>"""
    metric: NotRequired["aws_sdk_ec2.types.metric_type.MetricType"]
    """<p>The metric used for the network performance request.</p>"""
    statistic: NotRequired["aws_sdk_ec2.types.statistic_type.StatisticType"]
    """<p>The statistic used for the network performance request.</p>"""
    period: NotRequired["aws_sdk_ec2.types.period_type.PeriodType"]
    """<p>The period used for the network performance request.</p>"""
    metric_points: NotRequired["aws_sdk_ec2.types.metric_points.MetricPoints"]
    """<p>A list of <code>MetricPoint</code> objects.</p>"""
