"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeCapacityBlockOfferingsResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.capacity_block_offering_set
    import aws_sdk_ec2.types.string


class DescribeCapacityBlockOfferingsResult(TypedDict):
    capacity_block_offerings: NotRequired[
        "aws_sdk_ec2.types.capacity_block_offering_set.CapacityBlockOfferingSet"
    ]
    """<p>The recommended Capacity Block offering for the dates specified.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""
