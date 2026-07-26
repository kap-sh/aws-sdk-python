"""Generated from Smithy shape ``com.amazonaws.ec2#AvailabilityZoneGeographyList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.availability_zone_geography

AvailabilityZoneGeographyList: TypeAlias = list[
    "capo_ec2.types.availability_zone_geography.AvailabilityZoneGeography"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AvailabilityZoneGeographyList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.availability_zone_geography

        capo_ec2.types.availability_zone_geography.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> AvailabilityZoneGeographyList:
    import capo_ec2.types.availability_zone_geography

    out: AvailabilityZoneGeographyList = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.availability_zone_geography.deserialize_ec2_query(child)
        )
    return out
