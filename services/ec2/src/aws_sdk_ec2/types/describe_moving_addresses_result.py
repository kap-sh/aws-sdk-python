"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeMovingAddressesResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.moving_address_status_set
    import aws_sdk_ec2.types.string


class DescribeMovingAddressesResult(TypedDict):
    moving_address_statuses: NotRequired[
        "aws_sdk_ec2.types.moving_address_status_set.MovingAddressStatusSet"
    ]
    """<p>The status for each Elastic IP address.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""
