"""Generated from Smithy shape ``com.amazonaws.ec2#CapacityReservationSet``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.capacity_reservation

CapacityReservationSet: TypeAlias = list[
    "capo_ec2.types.capacity_reservation.CapacityReservation"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CapacityReservationSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.capacity_reservation

        capo_ec2.types.capacity_reservation.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> CapacityReservationSet:
    import capo_ec2.types.capacity_reservation

    out: CapacityReservationSet = []
    for child in el.findall("item"):
        out.append(capo_ec2.types.capacity_reservation.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> CapacityReservationSet:
    import capo_ec2.types.capacity_reservation

    out: CapacityReservationSet = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.capacity_reservation.deserialize_ec2_query(child))
    return out
