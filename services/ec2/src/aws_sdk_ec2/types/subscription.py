"""Generated from Smithy shape ``com.amazonaws.ec2#Subscription``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.metric_type
    import aws_sdk_ec2.types.period_type
    import aws_sdk_ec2.types.statistic_type
    import aws_sdk_ec2.types.string


class Subscription(TypedDict):
    source: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Region or Availability Zone that's the source for the subscription. For example, <code>us-east-1</code>.</p>"""
    destination: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Region or Availability Zone that's the target for the subscription. For example, <code>eu-west-1</code>.</p>"""
    metric: NotRequired["aws_sdk_ec2.types.metric_type.MetricType"]
    """<p>The metric used for the subscription.</p>"""
    statistic: NotRequired["aws_sdk_ec2.types.statistic_type.StatisticType"]
    """<p>The statistic used for the subscription.</p>"""
    period: NotRequired["aws_sdk_ec2.types.period_type.PeriodType"]
    """<p>The data aggregation time for the subscription.</p>"""
