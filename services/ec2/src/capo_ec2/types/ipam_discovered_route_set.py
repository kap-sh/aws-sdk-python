"""Generated from Smithy shape ``com.amazonaws.ec2#IpamDiscoveredRouteSet``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.ipam_discovered_route

IpamDiscoveredRouteSet: TypeAlias = list[
    "capo_ec2.types.ipam_discovered_route.IpamDiscoveredRoute"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: IpamDiscoveredRouteSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.ipam_discovered_route

        capo_ec2.types.ipam_discovered_route.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> IpamDiscoveredRouteSet:
    import capo_ec2.types.ipam_discovered_route

    out: IpamDiscoveredRouteSet = []
    for child in el.findall("item"):
        out.append(capo_ec2.types.ipam_discovered_route.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> IpamDiscoveredRouteSet:
    import capo_ec2.types.ipam_discovered_route

    out: IpamDiscoveredRouteSet = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.ipam_discovered_route.deserialize_ec2_query(child))
    return out
