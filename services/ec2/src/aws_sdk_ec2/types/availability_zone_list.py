"""Generated from Smithy shape ``com.amazonaws.ec2#AvailabilityZoneList``."""

from typing import TYPE_CHECKING, TypeAlias
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.availability_zone

AvailabilityZoneList: TypeAlias = list[
    "aws_sdk_ec2.types.availability_zone.AvailabilityZone"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AvailabilityZoneList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.availability_zone

        aws_sdk_ec2.types.availability_zone.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> AvailabilityZoneList:
    import aws_sdk_ec2.types.availability_zone

    out: AvailabilityZoneList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_ec2.types.availability_zone.deserialize_ec2_query(child))
    return out
