"""Generated from Smithy shape ``com.amazonaws.ec2#EnableAwsNetworkPerformanceMetricSubscriptionRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.metric_type
    import aws_sdk_ec2.types.statistic_type
    import aws_sdk_ec2.types.string


class EnableAwsNetworkPerformanceMetricSubscriptionRequest(TypedDict):
    source: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The source Region (like <code>us-east-1</code>) or Availability Zone ID (like <code>use1-az1</code>) that the metric subscription is enabled for. If you use Availability Zone IDs, the Source and Destination Availability Zones must be in the same Region.</p>"""
    destination: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The target Region (like <code>us-east-2</code>) or Availability Zone ID (like <code>use2-az2</code>) that the metric subscription is enabled for. If you use Availability Zone IDs, the Source and Destination Availability Zones must be in the same Region.</p>"""
    metric: NotRequired["aws_sdk_ec2.types.metric_type.MetricType"]
    """<p>The metric used for the enabled subscription.</p>"""
    statistic: NotRequired["aws_sdk_ec2.types.statistic_type.StatisticType"]
    """<p>The statistic used for the enabled subscription.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
