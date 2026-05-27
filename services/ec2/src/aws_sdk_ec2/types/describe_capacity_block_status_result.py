"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeCapacityBlockStatusResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.capacity_block_status_set
    import aws_sdk_ec2.types.string


class DescribeCapacityBlockStatusResult(TypedDict):
    capacity_block_statuses: NotRequired[
        "aws_sdk_ec2.types.capacity_block_status_set.CapacityBlockStatusSet"
    ]
    """<p>The availability of capacity for a Capacity Block.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""
