"""Generated from Smithy shape ``com.amazonaws.ec2#ReservedInstanceReservationValueSet``."""

from typing import TYPE_CHECKING, TypeAlias
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.reserved_instance_reservation_value

ReservedInstanceReservationValueSet: TypeAlias = list[
    "aws_sdk_ec2.types.reserved_instance_reservation_value.ReservedInstanceReservationValue"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ReservedInstanceReservationValueSet,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.reserved_instance_reservation_value

        aws_sdk_ec2.types.reserved_instance_reservation_value.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(
    parent: Element, tag: str
) -> ReservedInstanceReservationValueSet:
    import aws_sdk_ec2.types.reserved_instance_reservation_value

    out: ReservedInstanceReservationValueSet = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_ec2.types.reserved_instance_reservation_value.deserialize_ec2_query(
                child
            )
        )
    return out
