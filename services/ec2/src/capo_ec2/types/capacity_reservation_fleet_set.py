"""Generated from Smithy shape ``com.amazonaws.ec2#CapacityReservationFleetSet``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.capacity_reservation_fleet

CapacityReservationFleetSet: TypeAlias = list[
    "capo_ec2.types.capacity_reservation_fleet.CapacityReservationFleet"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CapacityReservationFleetSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.capacity_reservation_fleet

        capo_ec2.types.capacity_reservation_fleet.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> CapacityReservationFleetSet:
    import capo_ec2.types.capacity_reservation_fleet

    out: CapacityReservationFleetSet = []
    for child in el.findall("item"):
        out.append(
            capo_ec2.types.capacity_reservation_fleet.deserialize_ec2_query(child)
        )
    return out


def deserialize_ec2_query_flat(
    parent: Element, tag: str
) -> CapacityReservationFleetSet:
    import capo_ec2.types.capacity_reservation_fleet

    out: CapacityReservationFleetSet = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.capacity_reservation_fleet.deserialize_ec2_query(child)
        )
    return out
