"""Generated from Smithy shape ``com.amazonaws.ec2#ReservationTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.fleet_reservation_type

ReservationTypeList: TypeAlias = list[
    "capo_ec2.types.fleet_reservation_type.FleetReservationType"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ReservationTypeList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.fleet_reservation_type

        capo_ec2.types.fleet_reservation_type.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> ReservationTypeList:
    import capo_ec2.types.fleet_reservation_type

    out: ReservationTypeList = []
    for child in el.findall("item"):
        out.append(capo_ec2.types.fleet_reservation_type.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> ReservationTypeList:
    import capo_ec2.types.fleet_reservation_type

    out: ReservationTypeList = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.fleet_reservation_type.deserialize_ec2_query(child))
    return out
