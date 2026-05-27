"""Generated from Smithy shape ``com.amazonaws.ec2#CapacityBlockStatus``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.capacity_block_id
    import aws_sdk_ec2.types.capacity_block_interconnect_status
    import aws_sdk_ec2.types.capacity_reservation_status_set
    import aws_sdk_ec2.types.integer


class CapacityBlockStatus(TypedDict):
    capacity_block_id: NotRequired[
        "aws_sdk_ec2.types.capacity_block_id.CapacityBlockId"
    ]
    """<p>The ID of the Capacity Block.</p>"""
    interconnect_status: NotRequired[
        "aws_sdk_ec2.types.capacity_block_interconnect_status.CapacityBlockInterconnectStatus"
    ]
    """<p>The status of the high-bandwidth accelerator interconnect. Possible states include:</p> <ul> <li> <p> <code>ok</code> the accelerator interconnect is healthy.</p> </li> <li> <p> <code>impaired</code> - accelerator interconnect communication is impaired.</p> </li> <li> <p> <code>insufficient-data</code> - insufficient data to determine accelerator interconnect status.</p> </li> </ul>"""
    total_capacity: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The combined amount of <code>Available</code> and <code>Unavailable</code> capacity in the Capacity Block.</p>"""
    total_available_capacity: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The remaining capacity. Indicates the number of resources that can be launched into the Capacity Block.</p>"""
    total_unavailable_capacity: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The unavailable capacity. Indicates the instance capacity that is unavailable for use due to a system status check failure.</p>"""
    capacity_reservation_statuses: NotRequired[
        "aws_sdk_ec2.types.capacity_reservation_status_set.CapacityReservationStatusSet"
    ]
    """<p>The availability of capacity for the Capacity Block reservations.</p>"""
