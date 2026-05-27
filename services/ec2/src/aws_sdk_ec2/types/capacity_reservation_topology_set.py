"""Generated from Smithy shape ``com.amazonaws.ec2#CapacityReservationTopologySet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.capacity_reservation_topology

CapacityReservationTopologySet: TypeAlias = list[
    "aws_sdk_ec2.types.capacity_reservation_topology.CapacityReservationTopology"
]
