"""Generated from Smithy shape ``com.amazonaws.ec2#UpdateInterruptibleCapacityReservationAllocationRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.capacity_reservation_id
    import aws_sdk_ec2.types.integer


class UpdateInterruptibleCapacityReservationAllocationRequest(TypedDict):
    capacity_reservation_id: NotRequired[
        "aws_sdk_ec2.types.capacity_reservation_id.CapacityReservationId"
    ]
    """<p> The ID of the source Capacity Reservation containing the interruptible allocation to modify. </p>"""
    target_instance_count: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p> The new number of instances to allocate. Enter a higher number to add more capacity to share, or a lower number to reclaim capacity to your source Capacity Reservation. </p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p> Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. </p>"""
