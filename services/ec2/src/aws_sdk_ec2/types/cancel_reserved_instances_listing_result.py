"""Generated from Smithy shape ``com.amazonaws.ec2#CancelReservedInstancesListingResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.reserved_instances_listing_list


class CancelReservedInstancesListingResult(TypedDict):
    reserved_instances_listings: NotRequired[
        "aws_sdk_ec2.types.reserved_instances_listing_list.ReservedInstancesListingList"
    ]
    """<p>The Reserved Instance listing.</p>"""
