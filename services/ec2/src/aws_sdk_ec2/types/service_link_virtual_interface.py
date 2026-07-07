"""Generated from Smithy shape ``com.amazonaws.ec2#ServiceLinkVirtualInterface``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.long
    import aws_sdk_ec2.types.outpost_lag_id
    import aws_sdk_ec2.types.resource_arn
    import aws_sdk_ec2.types.service_link_virtual_interface_configuration_state
    import aws_sdk_ec2.types.service_link_virtual_interface_id
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list


class ServiceLinkVirtualInterface(TypedDict, closed=True):
    service_link_virtual_interface_id: NotRequired[
        "aws_sdk_ec2.types.service_link_virtual_interface_id.ServiceLinkVirtualInterfaceId"
    ]
    """<p>The ID of the service link virtual interface.</p>"""
    service_link_virtual_interface_arn: NotRequired[
        "aws_sdk_ec2.types.resource_arn.ResourceArn"
    ]
    """<p>The Amazon Resource Number (ARN) for the service link virtual interface. </p>"""
    outpost_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Outpost ID for the service link virtual interface.</p>"""
    outpost_arn: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Outpost Amazon Resource Number (ARN) for the service link virtual interface.</p>"""
    owner_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Amazon Web Services account that owns the service link virtual interface..</p>"""
    local_address: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The IPv4 address assigned to the local gateway virtual interface on the Outpost side.</p>"""
    peer_address: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The IPv4 peer address for the service link virtual interface.</p>"""
    peer_bgp_asn: NotRequired["aws_sdk_ec2.types.long.Long"]
    """<p>The ASN for the Border Gateway Protocol (BGP) associated with the service link virtual interface.</p>"""
    vlan: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The virtual local area network for the service link virtual interface.</p>"""
    outpost_lag_id: NotRequired["aws_sdk_ec2.types.outpost_lag_id.OutpostLagId"]
    """<p>The link aggregation group (LAG) ID for the service link virtual interface.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>The tags associated with the service link virtual interface.</p>"""
    configuration_state: NotRequired[
        "aws_sdk_ec2.types.service_link_virtual_interface_configuration_state.ServiceLinkVirtualInterfaceConfigurationState"
    ]
    """<p>The current state of the service link virtual interface.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ServiceLinkVirtualInterface, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "service_link_virtual_interface_id" in value:
        pairs.append(
            (
                f"{prefix}.ServiceLinkVirtualInterfaceId",
                str(value["service_link_virtual_interface_id"]),
            )
        )
    if "service_link_virtual_interface_arn" in value:
        pairs.append(
            (
                f"{prefix}.ServiceLinkVirtualInterfaceArn",
                str(value["service_link_virtual_interface_arn"]),
            )
        )
    if "outpost_id" in value:
        pairs.append((f"{prefix}.OutpostId", str(value["outpost_id"])))
    if "outpost_arn" in value:
        pairs.append((f"{prefix}.OutpostArn", str(value["outpost_arn"])))
    if "owner_id" in value:
        pairs.append((f"{prefix}.OwnerId", str(value["owner_id"])))
    if "local_address" in value:
        pairs.append((f"{prefix}.LocalAddress", str(value["local_address"])))
    if "peer_address" in value:
        pairs.append((f"{prefix}.PeerAddress", str(value["peer_address"])))
    if "peer_bgp_asn" in value:
        pairs.append((f"{prefix}.PeerBgpAsn", str(value["peer_bgp_asn"])))
    if "vlan" in value:
        pairs.append((f"{prefix}.Vlan", str(value["vlan"])))
    if "outpost_lag_id" in value:
        pairs.append((f"{prefix}.OutpostLagId", str(value["outpost_lag_id"])))
    if "tags" in value:
        import aws_sdk_ec2.types.tag_list

        aws_sdk_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{prefix}.TagSet"
        )
    if "configuration_state" in value:
        import aws_sdk_ec2.types.service_link_virtual_interface_configuration_state

        aws_sdk_ec2.types.service_link_virtual_interface_configuration_state.serialize_ec2_query(
            value["configuration_state"], pairs, f"{prefix}.ConfigurationState"
        )


def deserialize_ec2_query(el: Element) -> ServiceLinkVirtualInterface:
    out: ServiceLinkVirtualInterface = {}  # type: ignore[typeddict-item]
    child_service_link_virtual_interface_id = el.find("ServiceLinkVirtualInterfaceId")
    if child_service_link_virtual_interface_id is not None:
        out["service_link_virtual_interface_id"] = str(
            child_service_link_virtual_interface_id.text or ""
        )
    child_service_link_virtual_interface_arn = el.find("ServiceLinkVirtualInterfaceArn")
    if child_service_link_virtual_interface_arn is not None:
        out["service_link_virtual_interface_arn"] = str(
            child_service_link_virtual_interface_arn.text or ""
        )
    child_outpost_id = el.find("OutpostId")
    if child_outpost_id is not None:
        out["outpost_id"] = str(child_outpost_id.text or "")
    child_outpost_arn = el.find("OutpostArn")
    if child_outpost_arn is not None:
        out["outpost_arn"] = str(child_outpost_arn.text or "")
    child_owner_id = el.find("OwnerId")
    if child_owner_id is not None:
        out["owner_id"] = str(child_owner_id.text or "")
    child_local_address = el.find("LocalAddress")
    if child_local_address is not None:
        out["local_address"] = str(child_local_address.text or "")
    child_peer_address = el.find("PeerAddress")
    if child_peer_address is not None:
        out["peer_address"] = str(child_peer_address.text or "")
    child_peer_bgp_asn = el.find("PeerBgpAsn")
    if child_peer_bgp_asn is not None:
        out["peer_bgp_asn"] = int(child_peer_bgp_asn.text or "")
    child_vlan = el.find("Vlan")
    if child_vlan is not None:
        out["vlan"] = int(child_vlan.text or "")
    child_outpost_lag_id = el.find("OutpostLagId")
    if child_outpost_lag_id is not None:
        out["outpost_lag_id"] = str(child_outpost_lag_id.text or "")
    if el.find("TagSet") is not None:
        import aws_sdk_ec2.types.tag_list

        out["tags"] = aws_sdk_ec2.types.tag_list.deserialize_ec2_query(el, "TagSet")
    child_configuration_state = el.find("ConfigurationState")
    if child_configuration_state is not None:
        import aws_sdk_ec2.types.service_link_virtual_interface_configuration_state

        out["configuration_state"] = (
            aws_sdk_ec2.types.service_link_virtual_interface_configuration_state.deserialize_ec2_query(
                child_configuration_state
            )
        )
    return out
