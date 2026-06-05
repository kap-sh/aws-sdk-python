"""Generated from Smithy shape ``com.amazonaws.ec2#FleetCapacityReservationSet``."""

from typing import TYPE_CHECKING, TypeAlias
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.fleet_capacity_reservation

FleetCapacityReservationSet: TypeAlias = list[
    "aws_sdk_ec2.types.fleet_capacity_reservation.FleetCapacityReservation"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: FleetCapacityReservationSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.fleet_capacity_reservation

        aws_sdk_ec2.types.fleet_capacity_reservation.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> FleetCapacityReservationSet:
    import aws_sdk_ec2.types.fleet_capacity_reservation

    out: FleetCapacityReservationSet = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_ec2.types.fleet_capacity_reservation.deserialize_ec2_query(child)
        )
    return out
