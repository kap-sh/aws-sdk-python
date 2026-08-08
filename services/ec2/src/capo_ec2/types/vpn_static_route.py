"""Generated from Smithy shape ``com.amazonaws.ec2#VpnStaticRoute``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.string
    import capo_ec2.types.vpn_state
    import capo_ec2.types.vpn_static_route_source


class VpnStaticRoute(TypedDict, closed=True):
    destination_cidr_block: NotRequired["capo_ec2.types.string.String"]
    """<p>The CIDR block associated with the local subnet of the customer data center.</p>"""
    source: NotRequired["capo_ec2.types.vpn_static_route_source.VpnStaticRouteSource"]
    """<p>Indicates how the routes were provided.</p>"""
    state: NotRequired["capo_ec2.types.vpn_state.VpnState"]
    """<p>The current state of the static route.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: VpnStaticRoute, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "destination_cidr_block" in value:
        pairs.append(
            (f"{key_prefix}DestinationCidrBlock", str(value["destination_cidr_block"]))
        )
    if "source" in value:
        import capo_ec2.types.vpn_static_route_source

        capo_ec2.types.vpn_static_route_source.serialize_ec2_query(
            value["source"], pairs, f"{key_prefix}Source"
        )
    if "state" in value:
        import capo_ec2.types.vpn_state

        capo_ec2.types.vpn_state.serialize_ec2_query(
            value["state"], pairs, f"{key_prefix}State"
        )


def deserialize_ec2_query(el: Element) -> VpnStaticRoute:
    out: VpnStaticRoute = {}  # type: ignore[typeddict-item]
    child_destination_cidr_block = el.find("destinationCidrBlock")
    if child_destination_cidr_block is not None:
        out["destination_cidr_block"] = str(child_destination_cidr_block.text or "")
    child_source = el.find("source")
    if child_source is not None:
        import capo_ec2.types.vpn_static_route_source

        out["source"] = capo_ec2.types.vpn_static_route_source.deserialize_ec2_query(
            child_source
        )
    child_state = el.find("state")
    if child_state is not None:
        import capo_ec2.types.vpn_state

        out["state"] = capo_ec2.types.vpn_state.deserialize_ec2_query(child_state)
    return out
