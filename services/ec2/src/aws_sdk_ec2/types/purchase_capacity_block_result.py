"""Generated from Smithy shape ``com.amazonaws.ec2#PurchaseCapacityBlockResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.capacity_block_set
    import aws_sdk_ec2.types.capacity_reservation


class PurchaseCapacityBlockResult(TypedDict):
    capacity_reservation: NotRequired[
        "aws_sdk_ec2.types.capacity_reservation.CapacityReservation"
    ]
    """<p>The Capacity Reservation.</p>"""
    capacity_blocks: NotRequired[
        "aws_sdk_ec2.types.capacity_block_set.CapacityBlockSet"
    ]
    """<p>The Capacity Block.</p>"""
