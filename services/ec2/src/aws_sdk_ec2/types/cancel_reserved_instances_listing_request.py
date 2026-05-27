"""Generated from Smithy shape ``com.amazonaws.ec2#CancelReservedInstancesListingRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.reserved_instances_listing_id


class CancelReservedInstancesListingRequest(TypedDict):
    reserved_instances_listing_id: NotRequired[
        "aws_sdk_ec2.types.reserved_instances_listing_id.ReservedInstancesListingId"
    ]
    """<p>The ID of the Reserved Instance listing.</p>"""
