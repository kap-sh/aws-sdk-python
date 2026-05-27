"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeInstancesResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.reservation_list
    import aws_sdk_ec2.types.string


class DescribeInstancesResult(TypedDict):
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""
    reservations: NotRequired["aws_sdk_ec2.types.reservation_list.ReservationList"]
    """<p>Information about the reservations.</p>"""
