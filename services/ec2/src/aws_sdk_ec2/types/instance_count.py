"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceCount``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.listing_state


class InstanceCount(TypedDict):
    instance_count: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The number of listed Reserved Instances in the state specified by the <code>state</code>.</p>"""
    state: NotRequired["aws_sdk_ec2.types.listing_state.ListingState"]
    """<p>The states of the listed Reserved Instances.</p>"""
