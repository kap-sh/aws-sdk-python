"""Generated from Smithy shape ``com.amazonaws.ec2#LocalGatewayVirtualInterface``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.integer
    import capo_ec2.types.local_gateway_virtual_interface_configuration_state
    import capo_ec2.types.local_gateway_virtual_interface_group_id
    import capo_ec2.types.local_gateway_virtual_interface_id
    import capo_ec2.types.long
    import capo_ec2.types.resource_arn
    import capo_ec2.types.string
    import capo_ec2.types.tag_list


class LocalGatewayVirtualInterface(TypedDict, closed=True):
    local_gateway_virtual_interface_id: NotRequired[
        "capo_ec2.types.local_gateway_virtual_interface_id.LocalGatewayVirtualInterfaceId"
    ]
    """<p>The ID of the virtual interface.</p>"""
    local_gateway_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the local gateway.</p>"""
    local_gateway_virtual_interface_group_id: NotRequired[
        "capo_ec2.types.local_gateway_virtual_interface_group_id.LocalGatewayVirtualInterfaceGroupId"
    ]
    """<p>The ID of the local gateway virtual interface group.</p>"""
    local_gateway_virtual_interface_arn: NotRequired[
        "capo_ec2.types.resource_arn.ResourceArn"
    ]
    """<p>The Amazon Resource Number (ARN) of the local gateway virtual interface.</p>"""
    outpost_lag_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The Outpost LAG ID.</p>"""
    vlan: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The ID of the VLAN.</p>"""
    local_address: NotRequired["capo_ec2.types.string.String"]
    """<p>The local address.</p>"""
    peer_address: NotRequired["capo_ec2.types.string.String"]
    """<p>The peer address.</p>"""
    local_bgp_asn: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The Border Gateway Protocol (BGP) Autonomous System Number (ASN) of the local gateway.</p>"""
    peer_bgp_asn: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The peer BGP ASN.</p>"""
    peer_bgp_asn_extended: NotRequired["capo_ec2.types.long.Long"]
    """<p>The extended 32-bit ASN of the BGP peer for use with larger ASN values.</p>"""
    owner_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the Amazon Web Services account that owns the local gateway virtual interface.</p>"""
    tags: NotRequired["capo_ec2.types.tag_list.TagList"]
    """<p>The tags assigned to the virtual interface.</p>"""
    configuration_state: NotRequired[
        "capo_ec2.types.local_gateway_virtual_interface_configuration_state.LocalGatewayVirtualInterfaceConfigurationState"
    ]
    """<p>The current state of the local gateway virtual interface.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: LocalGatewayVirtualInterface, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "local_gateway_virtual_interface_id" in value:
        pairs.append(
            (
                f"{key_prefix}LocalGatewayVirtualInterfaceId",
                str(value["local_gateway_virtual_interface_id"]),
            )
        )
    if "local_gateway_id" in value:
        pairs.append((f"{key_prefix}LocalGatewayId", str(value["local_gateway_id"])))
    if "local_gateway_virtual_interface_group_id" in value:
        pairs.append(
            (
                f"{key_prefix}LocalGatewayVirtualInterfaceGroupId",
                str(value["local_gateway_virtual_interface_group_id"]),
            )
        )
    if "local_gateway_virtual_interface_arn" in value:
        pairs.append(
            (
                f"{key_prefix}LocalGatewayVirtualInterfaceArn",
                str(value["local_gateway_virtual_interface_arn"]),
            )
        )
    if "outpost_lag_id" in value:
        pairs.append((f"{key_prefix}OutpostLagId", str(value["outpost_lag_id"])))
    if "vlan" in value:
        pairs.append((f"{key_prefix}Vlan", str(value["vlan"])))
    if "local_address" in value:
        pairs.append((f"{key_prefix}LocalAddress", str(value["local_address"])))
    if "peer_address" in value:
        pairs.append((f"{key_prefix}PeerAddress", str(value["peer_address"])))
    if "local_bgp_asn" in value:
        pairs.append((f"{key_prefix}LocalBgpAsn", str(value["local_bgp_asn"])))
    if "peer_bgp_asn" in value:
        pairs.append((f"{key_prefix}PeerBgpAsn", str(value["peer_bgp_asn"])))
    if "peer_bgp_asn_extended" in value:
        pairs.append(
            (f"{key_prefix}PeerBgpAsnExtended", str(value["peer_bgp_asn_extended"]))
        )
    if "owner_id" in value:
        pairs.append((f"{key_prefix}OwnerId", str(value["owner_id"])))
    if "tags" in value:
        import capo_ec2.types.tag_list

        capo_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{key_prefix}TagSet"
        )
    if "configuration_state" in value:
        import capo_ec2.types.local_gateway_virtual_interface_configuration_state

        capo_ec2.types.local_gateway_virtual_interface_configuration_state.serialize_ec2_query(
            value["configuration_state"], pairs, f"{key_prefix}ConfigurationState"
        )


def deserialize_ec2_query(el: Element) -> LocalGatewayVirtualInterface:
    out: LocalGatewayVirtualInterface = {}  # type: ignore[typeddict-item]
    child_local_gateway_virtual_interface_id = el.find("localGatewayVirtualInterfaceId")
    if child_local_gateway_virtual_interface_id is not None:
        out["local_gateway_virtual_interface_id"] = str(
            child_local_gateway_virtual_interface_id.text or ""
        )
    child_local_gateway_id = el.find("localGatewayId")
    if child_local_gateway_id is not None:
        out["local_gateway_id"] = str(child_local_gateway_id.text or "")
    child_local_gateway_virtual_interface_group_id = el.find(
        "localGatewayVirtualInterfaceGroupId"
    )
    if child_local_gateway_virtual_interface_group_id is not None:
        out["local_gateway_virtual_interface_group_id"] = str(
            child_local_gateway_virtual_interface_group_id.text or ""
        )
    child_local_gateway_virtual_interface_arn = el.find(
        "localGatewayVirtualInterfaceArn"
    )
    if child_local_gateway_virtual_interface_arn is not None:
        out["local_gateway_virtual_interface_arn"] = str(
            child_local_gateway_virtual_interface_arn.text or ""
        )
    child_outpost_lag_id = el.find("outpostLagId")
    if child_outpost_lag_id is not None:
        out["outpost_lag_id"] = str(child_outpost_lag_id.text or "")
    child_vlan = el.find("vlan")
    if child_vlan is not None:
        out["vlan"] = int(child_vlan.text or "")
    child_local_address = el.find("localAddress")
    if child_local_address is not None:
        out["local_address"] = str(child_local_address.text or "")
    child_peer_address = el.find("peerAddress")
    if child_peer_address is not None:
        out["peer_address"] = str(child_peer_address.text or "")
    child_local_bgp_asn = el.find("localBgpAsn")
    if child_local_bgp_asn is not None:
        out["local_bgp_asn"] = int(child_local_bgp_asn.text or "")
    child_peer_bgp_asn = el.find("peerBgpAsn")
    if child_peer_bgp_asn is not None:
        out["peer_bgp_asn"] = int(child_peer_bgp_asn.text or "")
    child_peer_bgp_asn_extended = el.find("peerBgpAsnExtended")
    if child_peer_bgp_asn_extended is not None:
        out["peer_bgp_asn_extended"] = int(child_peer_bgp_asn_extended.text or "")
    child_owner_id = el.find("ownerId")
    if child_owner_id is not None:
        out["owner_id"] = str(child_owner_id.text or "")
    if el.find("tagSet") is not None:
        import capo_ec2.types.tag_list

        out["tags"] = capo_ec2.types.tag_list.deserialize_ec2_query(el, "tagSet")
    child_configuration_state = el.find("configurationState")
    if child_configuration_state is not None:
        import capo_ec2.types.local_gateway_virtual_interface_configuration_state

        out["configuration_state"] = (
            capo_ec2.types.local_gateway_virtual_interface_configuration_state.deserialize_ec2_query(
                child_configuration_state
            )
        )
    return out
