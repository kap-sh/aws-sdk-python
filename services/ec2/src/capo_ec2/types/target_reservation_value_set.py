"""Generated from Smithy shape ``com.amazonaws.ec2#TargetReservationValueSet``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.target_reservation_value

TargetReservationValueSet: TypeAlias = list[
    "capo_ec2.types.target_reservation_value.TargetReservationValue"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: TargetReservationValueSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.target_reservation_value

        capo_ec2.types.target_reservation_value.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> TargetReservationValueSet:
    import capo_ec2.types.target_reservation_value

    out: TargetReservationValueSet = []
    for child in el.findall("item"):
        out.append(capo_ec2.types.target_reservation_value.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> TargetReservationValueSet:
    import capo_ec2.types.target_reservation_value

    out: TargetReservationValueSet = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.target_reservation_value.deserialize_ec2_query(child))
    return out
