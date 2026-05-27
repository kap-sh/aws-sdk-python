"""Generated from Smithy shape ``com.amazonaws.ec2#ReservedInstancesListingList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.reserved_instances_listing

ReservedInstancesListingList: TypeAlias = list[
    "aws_sdk_ec2.types.reserved_instances_listing.ReservedInstancesListing"
]
