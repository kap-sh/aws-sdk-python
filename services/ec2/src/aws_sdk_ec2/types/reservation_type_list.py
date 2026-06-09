"""Generated from Smithy shape ``com.amazonaws.ec2#ReservationTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.fleet_reservation_type

ReservationTypeList: TypeAlias = list[
    "aws_sdk_ec2.types.fleet_reservation_type.FleetReservationType"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ReservationTypeList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.fleet_reservation_type

        aws_sdk_ec2.types.fleet_reservation_type.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> ReservationTypeList:
    import aws_sdk_ec2.types.fleet_reservation_type

    out: ReservationTypeList = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_ec2.types.fleet_reservation_type.deserialize_ec2_query(child)
        )
    return out
