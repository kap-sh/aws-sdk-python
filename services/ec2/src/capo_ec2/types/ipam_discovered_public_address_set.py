"""Generated from Smithy shape ``com.amazonaws.ec2#IpamDiscoveredPublicAddressSet``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.ipam_discovered_public_address

IpamDiscoveredPublicAddressSet: TypeAlias = list[
    "capo_ec2.types.ipam_discovered_public_address.IpamDiscoveredPublicAddress"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: IpamDiscoveredPublicAddressSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.ipam_discovered_public_address

        capo_ec2.types.ipam_discovered_public_address.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> IpamDiscoveredPublicAddressSet:
    import capo_ec2.types.ipam_discovered_public_address

    out: IpamDiscoveredPublicAddressSet = []
    for child in el.findall("item"):
        out.append(
            capo_ec2.types.ipam_discovered_public_address.deserialize_ec2_query(child)
        )
    return out


def deserialize_ec2_query_flat(
    parent: Element, tag: str
) -> IpamDiscoveredPublicAddressSet:
    import capo_ec2.types.ipam_discovered_public_address

    out: IpamDiscoveredPublicAddressSet = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.ipam_discovered_public_address.deserialize_ec2_query(child)
        )
    return out
