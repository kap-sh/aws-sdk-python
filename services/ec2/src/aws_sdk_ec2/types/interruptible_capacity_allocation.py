"""Generated from Smithy shape ``com.amazonaws.ec2#InterruptibleCapacityAllocation``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.interruptible_capacity_reservation_allocation_status
    import aws_sdk_ec2.types.interruption_type
    import aws_sdk_ec2.types.string


class InterruptibleCapacityAllocation(TypedDict):
    instance_count: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p> The current number of instances allocated to the interruptible reservation. </p>"""
    target_instance_count: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p> After your modify request, the requested number of instances allocated to interruptible reservation. </p>"""
    status: NotRequired[
        "aws_sdk_ec2.types.interruptible_capacity_reservation_allocation_status.InterruptibleCapacityReservationAllocationStatus"
    ]
    """<p> The current status of the allocation (updating during reclamation, active when complete). </p>"""
    interruptible_capacity_reservation_id: NotRequired[
        "aws_sdk_ec2.types.string.String"
    ]
    """<p> The ID of the interruptible Capacity Reservation created from the allocation. </p>"""
    interruption_type: NotRequired[
        "aws_sdk_ec2.types.interruption_type.InterruptionType"
    ]
    """<p> The type of interruption policy applied to the interruptible reservation. </p>"""
