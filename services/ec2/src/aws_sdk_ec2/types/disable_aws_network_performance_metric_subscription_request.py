"""Generated from Smithy shape ``com.amazonaws.ec2#DisableAwsNetworkPerformanceMetricSubscriptionRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.metric_type
    import aws_sdk_ec2.types.statistic_type
    import aws_sdk_ec2.types.string


class DisableAwsNetworkPerformanceMetricSubscriptionRequest(TypedDict):
    source: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The source Region or Availability Zone that the metric subscription is disabled for. For example, <code>us-east-1</code>.</p>"""
    destination: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The target Region or Availability Zone that the metric subscription is disabled for. For example, <code>eu-north-1</code>.</p>"""
    metric: NotRequired["aws_sdk_ec2.types.metric_type.MetricType"]
    """<p>The metric used for the disabled subscription.</p>"""
    statistic: NotRequired["aws_sdk_ec2.types.statistic_type.StatisticType"]
    """<p>The statistic used for the disabled subscription. </p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
