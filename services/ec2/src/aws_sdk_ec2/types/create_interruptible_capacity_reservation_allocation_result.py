"""Generated from Smithy shape ``com.amazonaws.ec2#CreateInterruptibleCapacityReservationAllocationResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.capacity_reservation_id
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.interruptible_capacity_reservation_allocation_status
    import aws_sdk_ec2.types.interruption_type


class CreateInterruptibleCapacityReservationAllocationResult(TypedDict):
    source_capacity_reservation_id: NotRequired[
        "aws_sdk_ec2.types.capacity_reservation_id.CapacityReservationId"
    ]
    """<p> The ID of the source Capacity Reservation from which the interruptible Capacity Reservation was created. </p>"""
    target_instance_count: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p> The number of instances allocated to the interruptible reservation. </p>"""
    status: NotRequired[
        "aws_sdk_ec2.types.interruptible_capacity_reservation_allocation_status.InterruptibleCapacityReservationAllocationStatus"
    ]
    """<p> The current status of the allocation request (creating, active, updating). </p>"""
    interruption_type: NotRequired[
        "aws_sdk_ec2.types.interruption_type.InterruptionType"
    ]
    """<p> The type of interruption applied to the interruptible reservation. </p>"""
