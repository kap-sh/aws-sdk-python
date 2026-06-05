"""Generated from Smithy shape ``com.amazonaws.ec2#CapacityReservationTopologySet``."""

from typing import TYPE_CHECKING, TypeAlias
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.capacity_reservation_topology

CapacityReservationTopologySet: TypeAlias = list[
    "aws_sdk_ec2.types.capacity_reservation_topology.CapacityReservationTopology"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CapacityReservationTopologySet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.capacity_reservation_topology

        aws_sdk_ec2.types.capacity_reservation_topology.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> CapacityReservationTopologySet:
    import aws_sdk_ec2.types.capacity_reservation_topology

    out: CapacityReservationTopologySet = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_ec2.types.capacity_reservation_topology.deserialize_ec2_query(child)
        )
    return out
