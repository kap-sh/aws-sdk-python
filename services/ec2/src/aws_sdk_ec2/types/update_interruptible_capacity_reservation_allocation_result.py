"""Generated from Smithy shape ``com.amazonaws.ec2#UpdateInterruptibleCapacityReservationAllocationResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.capacity_reservation_id
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.interruptible_capacity_reservation_allocation_status
    import aws_sdk_ec2.types.interruption_type


class UpdateInterruptibleCapacityReservationAllocationResult(TypedDict):
    interruptible_capacity_reservation_id: NotRequired[
        "aws_sdk_ec2.types.capacity_reservation_id.CapacityReservationId"
    ]
    """<p> The ID of the interruptible Capacity Reservation that was modified. </p>"""
    source_capacity_reservation_id: NotRequired[
        "aws_sdk_ec2.types.capacity_reservation_id.CapacityReservationId"
    ]
    """<p> The ID of the source Capacity Reservation to which capacity was reclaimed or from which capacity was allocated. </p>"""
    instance_count: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p> The current number of instances allocated to the interruptible reservation. </p>"""
    target_instance_count: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p> The requested number of instances for the interruptible Capacity Reservation. </p>"""
    status: NotRequired[
        "aws_sdk_ec2.types.interruptible_capacity_reservation_allocation_status.InterruptibleCapacityReservationAllocationStatus"
    ]
    """<p> The current status of the allocation (updating during reclamation, active when complete). </p>"""
    interruption_type: NotRequired[
        "aws_sdk_ec2.types.interruption_type.InterruptionType"
    ]
    """<p> The interruption type for the interruptible reservation. </p>"""
