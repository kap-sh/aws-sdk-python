"""Generated from Smithy shape ``com.amazonaws.ec2#IpamDiscoveredResourceCidrSet``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.ipam_discovered_resource_cidr

IpamDiscoveredResourceCidrSet: TypeAlias = list[
    "capo_ec2.types.ipam_discovered_resource_cidr.IpamDiscoveredResourceCidr"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: IpamDiscoveredResourceCidrSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.ipam_discovered_resource_cidr

        capo_ec2.types.ipam_discovered_resource_cidr.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> IpamDiscoveredResourceCidrSet:
    import capo_ec2.types.ipam_discovered_resource_cidr

    out: IpamDiscoveredResourceCidrSet = []
    for child in el.findall("item"):
        out.append(
            capo_ec2.types.ipam_discovered_resource_cidr.deserialize_ec2_query(child)
        )
    return out


def deserialize_ec2_query_flat(
    parent: Element, tag: str
) -> IpamDiscoveredResourceCidrSet:
    import capo_ec2.types.ipam_discovered_resource_cidr

    out: IpamDiscoveredResourceCidrSet = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.ipam_discovered_resource_cidr.deserialize_ec2_query(child)
        )
    return out
