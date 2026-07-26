"""Generated from Smithy shape ``com.amazonaws.ec2#CreateLocalGatewayVirtualInterfaceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.integer
    import capo_ec2.types.local_gateway_virtual_interface_group_id
    import capo_ec2.types.long
    import capo_ec2.types.outpost_lag_id
    import capo_ec2.types.string
    import capo_ec2.types.tag_specification_list


class CreateLocalGatewayVirtualInterfaceRequest(TypedDict, closed=True):
    local_gateway_virtual_interface_group_id: NotRequired[
        "capo_ec2.types.local_gateway_virtual_interface_group_id.LocalGatewayVirtualInterfaceGroupId"
    ]
    """<p>The ID of the local gateway virtual interface group.</p>"""
    outpost_lag_id: NotRequired["capo_ec2.types.outpost_lag_id.OutpostLagId"]
    """<p>References the Link Aggregation Group (LAG) that connects the Outpost to on-premises network devices.</p>"""
    vlan: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The virtual local area network (VLAN) used for the local gateway virtual interface.</p>"""
    local_address: NotRequired["capo_ec2.types.string.String"]
    """<p>The IP address assigned to the local gateway virtual interface on the Outpost side. Only IPv4 is supported.</p>"""
    peer_address: NotRequired["capo_ec2.types.string.String"]
    """<p>The peer IP address for the local gateway virtual interface. Only IPv4 is supported.</p>"""
    peer_bgp_asn: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The Autonomous System Number (ASN) of the Border Gateway Protocol (BGP) peer.</p>"""
    tag_specifications: NotRequired[
        "capo_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>The tags to apply to a resource when the local gateway virtual interface is being created. </p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    peer_bgp_asn_extended: NotRequired["capo_ec2.types.long.Long"]
    """<p>The extended 32-bit ASN of the BGP peer for use with larger ASN values.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateLocalGatewayVirtualInterfaceRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "local_gateway_virtual_interface_group_id" in value:
        pairs.append(
            (
                f"{prefix}.LocalGatewayVirtualInterfaceGroupId",
                str(value["local_gateway_virtual_interface_group_id"]),
            )
        )
    if "outpost_lag_id" in value:
        pairs.append((f"{prefix}.OutpostLagId", str(value["outpost_lag_id"])))
    if "vlan" in value:
        pairs.append((f"{prefix}.Vlan", str(value["vlan"])))
    if "local_address" in value:
        pairs.append((f"{prefix}.LocalAddress", str(value["local_address"])))
    if "peer_address" in value:
        pairs.append((f"{prefix}.PeerAddress", str(value["peer_address"])))
    if "peer_bgp_asn" in value:
        pairs.append((f"{prefix}.PeerBgpAsn", str(value["peer_bgp_asn"])))
    if "tag_specifications" in value:
        import capo_ec2.types.tag_specification_list

        capo_ec2.types.tag_specification_list.serialize_ec2_query(
            value["tag_specifications"], pairs, f"{prefix}.TagSpecifications"
        )
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))
    if "peer_bgp_asn_extended" in value:
        pairs.append(
            (f"{prefix}.PeerBgpAsnExtended", str(value["peer_bgp_asn_extended"]))
        )


def deserialize_ec2_query(el: Element) -> CreateLocalGatewayVirtualInterfaceRequest:
    out: CreateLocalGatewayVirtualInterfaceRequest = {}  # type: ignore[typeddict-item]
    child_local_gateway_virtual_interface_group_id = el.find(
        "LocalGatewayVirtualInterfaceGroupId"
    )
    if child_local_gateway_virtual_interface_group_id is not None:
        out["local_gateway_virtual_interface_group_id"] = str(
            child_local_gateway_virtual_interface_group_id.text or ""
        )
    child_outpost_lag_id = el.find("OutpostLagId")
    if child_outpost_lag_id is not None:
        out["outpost_lag_id"] = str(child_outpost_lag_id.text or "")
    child_vlan = el.find("Vlan")
    if child_vlan is not None:
        out["vlan"] = int(child_vlan.text or "")
    child_local_address = el.find("LocalAddress")
    if child_local_address is not None:
        out["local_address"] = str(child_local_address.text or "")
    child_peer_address = el.find("PeerAddress")
    if child_peer_address is not None:
        out["peer_address"] = str(child_peer_address.text or "")
    child_peer_bgp_asn = el.find("PeerBgpAsn")
    if child_peer_bgp_asn is not None:
        out["peer_bgp_asn"] = int(child_peer_bgp_asn.text or "")
    if el.find("TagSpecifications") is not None:
        import capo_ec2.types.tag_specification_list

        out["tag_specifications"] = (
            capo_ec2.types.tag_specification_list.deserialize_ec2_query(
                el, "TagSpecifications"
            )
        )
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_peer_bgp_asn_extended = el.find("PeerBgpAsnExtended")
    if child_peer_bgp_asn_extended is not None:
        out["peer_bgp_asn_extended"] = int(child_peer_bgp_asn_extended.text or "")
    return out
