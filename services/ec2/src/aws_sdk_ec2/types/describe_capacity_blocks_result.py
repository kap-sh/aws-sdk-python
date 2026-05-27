"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeCapacityBlocksResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.capacity_block_set
    import aws_sdk_ec2.types.string


class DescribeCapacityBlocksResult(TypedDict):
    capacity_blocks: NotRequired[
        "aws_sdk_ec2.types.capacity_block_set.CapacityBlockSet"
    ]
    """<p>The Capacity Blocks.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""
