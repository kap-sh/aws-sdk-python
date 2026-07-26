"""Generated from Smithy shape ``com.amazonaws.ec2#VpnTunnelOptionsSpecificationsList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.vpn_tunnel_options_specification

VpnTunnelOptionsSpecificationsList: TypeAlias = list[
    "capo_ec2.types.vpn_tunnel_options_specification.VpnTunnelOptionsSpecification"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: VpnTunnelOptionsSpecificationsList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.vpn_tunnel_options_specification

        capo_ec2.types.vpn_tunnel_options_specification.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(
    parent: Element, tag: str
) -> VpnTunnelOptionsSpecificationsList:
    import capo_ec2.types.vpn_tunnel_options_specification

    out: VpnTunnelOptionsSpecificationsList = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.vpn_tunnel_options_specification.deserialize_ec2_query(child)
        )
    return out
