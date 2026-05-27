"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceUsage``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.string


class InstanceUsage(TypedDict):
    account_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Amazon Web Services account that is making use of the Capacity Reservation.</p>"""
    used_instance_count: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The number of instances the Amazon Web Services account currently has in the Capacity Reservation.</p>"""
