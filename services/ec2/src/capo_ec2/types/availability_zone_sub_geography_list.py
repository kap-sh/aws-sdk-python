"""Generated from Smithy shape ``com.amazonaws.ec2#AvailabilityZoneSubGeographyList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.availability_zone_sub_geography

AvailabilityZoneSubGeographyList: TypeAlias = list[
    "capo_ec2.types.availability_zone_sub_geography.AvailabilityZoneSubGeography"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AvailabilityZoneSubGeographyList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.availability_zone_sub_geography

        capo_ec2.types.availability_zone_sub_geography.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> AvailabilityZoneSubGeographyList:
    import capo_ec2.types.availability_zone_sub_geography

    out: AvailabilityZoneSubGeographyList = []
    for child in el.findall("item"):
        out.append(
            capo_ec2.types.availability_zone_sub_geography.deserialize_ec2_query(child)
        )
    return out


def deserialize_ec2_query_flat(
    parent: Element, tag: str
) -> AvailabilityZoneSubGeographyList:
    import capo_ec2.types.availability_zone_sub_geography

    out: AvailabilityZoneSubGeographyList = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.availability_zone_sub_geography.deserialize_ec2_query(child)
        )
    return out
