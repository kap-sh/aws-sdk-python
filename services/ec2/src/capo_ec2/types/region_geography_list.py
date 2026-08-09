"""Generated from Smithy shape ``com.amazonaws.ec2#RegionGeographyList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.region_geography

RegionGeographyList: TypeAlias = list["capo_ec2.types.region_geography.RegionGeography"]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: RegionGeographyList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.region_geography

        capo_ec2.types.region_geography.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> RegionGeographyList:
    import capo_ec2.types.region_geography

    out: RegionGeographyList = []
    for child in el.findall("item"):
        out.append(capo_ec2.types.region_geography.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> RegionGeographyList:
    import capo_ec2.types.region_geography

    out: RegionGeographyList = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.region_geography.deserialize_ec2_query(child))
    return out
