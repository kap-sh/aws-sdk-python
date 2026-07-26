"""Generated from Smithy shape ``com.amazonaws.ec2#ReservationList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.reservation

ReservationList: TypeAlias = list["capo_ec2.types.reservation.Reservation"]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ReservationList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.reservation

        capo_ec2.types.reservation.serialize_ec2_query(item, pairs, f"{prefix}.{n}")


def deserialize_ec2_query(parent: Element, tag: str) -> ReservationList:
    import capo_ec2.types.reservation

    out: ReservationList = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.reservation.deserialize_ec2_query(child))
    return out
