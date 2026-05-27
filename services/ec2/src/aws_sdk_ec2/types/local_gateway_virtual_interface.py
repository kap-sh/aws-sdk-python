"""Generated from Smithy shape ``com.amazonaws.ec2#LocalGatewayVirtualInterface``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.local_gateway_virtual_interface_configuration_state
    import aws_sdk_ec2.types.local_gateway_virtual_interface_group_id
    import aws_sdk_ec2.types.local_gateway_virtual_interface_id
    import aws_sdk_ec2.types.long
    import aws_sdk_ec2.types.resource_arn
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list


class LocalGatewayVirtualInterface(TypedDict):
    local_gateway_virtual_interface_id: NotRequired[
        "aws_sdk_ec2.types.local_gateway_virtual_interface_id.LocalGatewayVirtualInterfaceId"
    ]
    """<p>The ID of the virtual interface.</p>"""
    local_gateway_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the local gateway.</p>"""
    local_gateway_virtual_interface_group_id: NotRequired[
        "aws_sdk_ec2.types.local_gateway_virtual_interface_group_id.LocalGatewayVirtualInterfaceGroupId"
    ]
    """<p>The ID of the local gateway virtual interface group.</p>"""
    local_gateway_virtual_interface_arn: NotRequired[
        "aws_sdk_ec2.types.resource_arn.ResourceArn"
    ]
    """<p>The Amazon Resource Number (ARN) of the local gateway virtual interface.</p>"""
    outpost_lag_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Outpost LAG ID.</p>"""
    vlan: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The ID of the VLAN.</p>"""
    local_address: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The local address.</p>"""
    peer_address: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The peer address.</p>"""
    local_bgp_asn: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The Border Gateway Protocol (BGP) Autonomous System Number (ASN) of the local gateway.</p>"""
    peer_bgp_asn: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The peer BGP ASN.</p>"""
    peer_bgp_asn_extended: NotRequired["aws_sdk_ec2.types.long.Long"]
    """<p>The extended 32-bit ASN of the BGP peer for use with larger ASN values.</p>"""
    owner_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Amazon Web Services account that owns the local gateway virtual interface.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>The tags assigned to the virtual interface.</p>"""
    configuration_state: NotRequired[
        "aws_sdk_ec2.types.local_gateway_virtual_interface_configuration_state.LocalGatewayVirtualInterfaceConfigurationState"
    ]
    """<p>The current state of the local gateway virtual interface.</p>"""
