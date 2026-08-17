"""Generated from Smithy shape ``com.amazonaws.ec2#ReservedInstanceReservationValueSet``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.reserved_instance_reservation_value

ReservedInstanceReservationValueSet: TypeAlias = list[
    "capo_ec2.types.reserved_instance_reservation_value.ReservedInstanceReservationValue"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ReservedInstanceReservationValueSet,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if not value:
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.reserved_instance_reservation_value

        capo_ec2.types.reserved_instance_reservation_value.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> ReservedInstanceReservationValueSet:
    import capo_ec2.types.reserved_instance_reservation_value

    out: ReservedInstanceReservationValueSet = []
    for child in el.findall("item"):
        out.append(
            capo_ec2.types.reserved_instance_reservation_value.deserialize_ec2_query(
                child
            )
        )
    return out


def deserialize_ec2_query_flat(
    parent: Element, tag: str
) -> ReservedInstanceReservationValueSet:
    import capo_ec2.types.reserved_instance_reservation_value

    out: ReservedInstanceReservationValueSet = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.reserved_instance_reservation_value.deserialize_ec2_query(
                child
            )
        )
    return out
