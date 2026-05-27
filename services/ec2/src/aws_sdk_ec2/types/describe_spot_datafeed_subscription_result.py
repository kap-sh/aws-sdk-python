"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeSpotDatafeedSubscriptionResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.spot_datafeed_subscription


class DescribeSpotDatafeedSubscriptionResult(TypedDict):
    spot_datafeed_subscription: NotRequired[
        "aws_sdk_ec2.types.spot_datafeed_subscription.SpotDatafeedSubscription"
    ]
    """<p>The Spot Instance data feed subscription.</p>"""
