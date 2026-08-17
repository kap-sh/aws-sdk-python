"""Generated from Smithy shape ``com.amazonaws.ec2#VpnStaticRouteList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.vpn_static_route

VpnStaticRouteList: TypeAlias = list["capo_ec2.types.vpn_static_route.VpnStaticRoute"]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: VpnStaticRouteList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.vpn_static_route

        capo_ec2.types.vpn_static_route.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> VpnStaticRouteList:
    import capo_ec2.types.vpn_static_route

    out: VpnStaticRouteList = []
    for child in el.findall("item"):
        out.append(capo_ec2.types.vpn_static_route.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> VpnStaticRouteList:
    import capo_ec2.types.vpn_static_route

    out: VpnStaticRouteList = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.vpn_static_route.deserialize_ec2_query(child))
    return out
