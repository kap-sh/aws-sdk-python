"""Generated from Smithy shape ``com.amazonaws.ec2#SubnetCidrReservationList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.subnet_cidr_reservation

SubnetCidrReservationList: TypeAlias = list[
    "capo_ec2.types.subnet_cidr_reservation.SubnetCidrReservation"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: SubnetCidrReservationList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.subnet_cidr_reservation

        capo_ec2.types.subnet_cidr_reservation.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> SubnetCidrReservationList:
    import capo_ec2.types.subnet_cidr_reservation

    out: SubnetCidrReservationList = []
    for child in el.findall("item"):
        out.append(capo_ec2.types.subnet_cidr_reservation.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> SubnetCidrReservationList:
    import capo_ec2.types.subnet_cidr_reservation

    out: SubnetCidrReservationList = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.subnet_cidr_reservation.deserialize_ec2_query(child))
    return out
