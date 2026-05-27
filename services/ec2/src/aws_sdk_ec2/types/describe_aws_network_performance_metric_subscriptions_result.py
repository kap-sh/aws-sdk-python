"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeAwsNetworkPerformanceMetricSubscriptionsResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.subscription_list


class DescribeAwsNetworkPerformanceMetricSubscriptionsResult(TypedDict):
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""
    subscriptions: NotRequired["aws_sdk_ec2.types.subscription_list.SubscriptionList"]
    """<p>Describes the current Infrastructure Performance subscriptions.</p>"""
