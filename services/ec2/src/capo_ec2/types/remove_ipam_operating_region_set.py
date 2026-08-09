"""Generated from Smithy shape ``com.amazonaws.ec2#RemoveIpamOperatingRegionSet``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.remove_ipam_operating_region

RemoveIpamOperatingRegionSet: TypeAlias = list[
    "capo_ec2.types.remove_ipam_operating_region.RemoveIpamOperatingRegion"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: RemoveIpamOperatingRegionSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.remove_ipam_operating_region

        capo_ec2.types.remove_ipam_operating_region.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> RemoveIpamOperatingRegionSet:
    import capo_ec2.types.remove_ipam_operating_region

    out: RemoveIpamOperatingRegionSet = []
    for child in el.findall("member"):
        out.append(
            capo_ec2.types.remove_ipam_operating_region.deserialize_ec2_query(child)
        )
    return out


def deserialize_ec2_query_flat(
    parent: Element, tag: str
) -> RemoveIpamOperatingRegionSet:
    import capo_ec2.types.remove_ipam_operating_region

    out: RemoveIpamOperatingRegionSet = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.remove_ipam_operating_region.deserialize_ec2_query(child)
        )
    return out
