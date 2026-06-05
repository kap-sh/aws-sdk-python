"""Generated from Smithy shape ``com.amazonaws.ec2#SubnetCidrReservationList``."""

from typing import TYPE_CHECKING, TypeAlias
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.subnet_cidr_reservation

SubnetCidrReservationList: TypeAlias = list[
    "aws_sdk_ec2.types.subnet_cidr_reservation.SubnetCidrReservation"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: SubnetCidrReservationList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.subnet_cidr_reservation

        aws_sdk_ec2.types.subnet_cidr_reservation.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> SubnetCidrReservationList:
    import aws_sdk_ec2.types.subnet_cidr_reservation

    out: SubnetCidrReservationList = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_ec2.types.subnet_cidr_reservation.deserialize_ec2_query(child)
        )
    return out
