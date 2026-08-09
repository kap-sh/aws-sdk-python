"""Generated from Smithy shape ``com.amazonaws.ec2#EndpointSet``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.client_vpn_endpoint

EndpointSet: TypeAlias = list["capo_ec2.types.client_vpn_endpoint.ClientVpnEndpoint"]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: EndpointSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.client_vpn_endpoint

        capo_ec2.types.client_vpn_endpoint.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> EndpointSet:
    import capo_ec2.types.client_vpn_endpoint

    out: EndpointSet = []
    for child in el.findall("item"):
        out.append(capo_ec2.types.client_vpn_endpoint.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> EndpointSet:
    import capo_ec2.types.client_vpn_endpoint

    out: EndpointSet = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.client_vpn_endpoint.deserialize_ec2_query(child))
    return out
