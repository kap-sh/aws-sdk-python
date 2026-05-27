"""Generated from Smithy shape ``com.amazonaws.ec2#SpotDatafeedSubscription``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.datafeed_subscription_state
    import aws_sdk_ec2.types.spot_instance_state_fault
    import aws_sdk_ec2.types.string


class SpotDatafeedSubscription(TypedDict):
    bucket: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The name of the Amazon S3 bucket where the Spot Instance data feed is located.</p>"""
    fault: NotRequired[
        "aws_sdk_ec2.types.spot_instance_state_fault.SpotInstanceStateFault"
    ]
    """<p>The fault codes for the Spot Instance request, if any.</p>"""
    owner_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Amazon Web Services account ID of the account.</p>"""
    prefix: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The prefix for the data feed files.</p>"""
    state: NotRequired[
        "aws_sdk_ec2.types.datafeed_subscription_state.DatafeedSubscriptionState"
    ]
    """<p>The state of the Spot Instance data feed subscription.</p>"""
