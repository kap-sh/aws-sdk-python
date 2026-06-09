"""Generated from Smithy shape ``com.amazonaws.ec2#AvailabilityZoneGeographyList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.availability_zone_geography

AvailabilityZoneGeographyList: TypeAlias = list[
    "aws_sdk_ec2.types.availability_zone_geography.AvailabilityZoneGeography"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AvailabilityZoneGeographyList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.availability_zone_geography

        aws_sdk_ec2.types.availability_zone_geography.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> AvailabilityZoneGeographyList:
    import aws_sdk_ec2.types.availability_zone_geography

    out: AvailabilityZoneGeographyList = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_ec2.types.availability_zone_geography.deserialize_ec2_query(child)
        )
    return out
