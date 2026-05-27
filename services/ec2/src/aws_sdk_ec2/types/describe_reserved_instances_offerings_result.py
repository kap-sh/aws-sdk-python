"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeReservedInstancesOfferingsResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.reserved_instances_offering_list
    import aws_sdk_ec2.types.string


class DescribeReservedInstancesOfferingsResult(TypedDict):
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""
    reserved_instances_offerings: NotRequired[
        "aws_sdk_ec2.types.reserved_instances_offering_list.ReservedInstancesOfferingList"
    ]
    """<p>A list of Reserved Instances offerings.</p>"""
