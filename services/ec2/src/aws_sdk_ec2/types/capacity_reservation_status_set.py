"""Generated from Smithy shape ``com.amazonaws.ec2#CapacityReservationStatusSet``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.capacity_reservation_status

CapacityReservationStatusSet: TypeAlias = list[
    "aws_sdk_ec2.types.capacity_reservation_status.CapacityReservationStatus"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CapacityReservationStatusSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.capacity_reservation_status

        aws_sdk_ec2.types.capacity_reservation_status.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> CapacityReservationStatusSet:
    import aws_sdk_ec2.types.capacity_reservation_status

    out: CapacityReservationStatusSet = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_ec2.types.capacity_reservation_status.deserialize_ec2_query(child)
        )
    return out
