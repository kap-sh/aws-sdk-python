"""Generated from Smithy shape ``com.amazonaws.ec2#LocalGatewayVirtualInterfaceGroup``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.local_gateway_virtual_interface_group_configuration_state
    import aws_sdk_ec2.types.local_gateway_virtual_interface_group_id
    import aws_sdk_ec2.types.local_gateway_virtual_interface_id_set
    import aws_sdk_ec2.types.long
    import aws_sdk_ec2.types.resource_arn
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list


class LocalGatewayVirtualInterfaceGroup(TypedDict):
    local_gateway_virtual_interface_group_id: NotRequired[
        "aws_sdk_ec2.types.local_gateway_virtual_interface_group_id.LocalGatewayVirtualInterfaceGroupId"
    ]
    """<p>The ID of the virtual interface group.</p>"""
    local_gateway_virtual_interface_ids: NotRequired[
        "aws_sdk_ec2.types.local_gateway_virtual_interface_id_set.LocalGatewayVirtualInterfaceIdSet"
    ]
    """<p>The IDs of the virtual interfaces.</p>"""
    local_gateway_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the local gateway.</p>"""
    owner_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Amazon Web Services account that owns the local gateway virtual interface group.</p>"""
    local_bgp_asn: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The Autonomous System Number(ASN) for the local Border Gateway Protocol (BGP).</p>"""
    local_bgp_asn_extended: NotRequired["aws_sdk_ec2.types.long.Long"]
    """<p>The extended 32-bit ASN for the local BGP configuration.</p>"""
    local_gateway_virtual_interface_group_arn: NotRequired[
        "aws_sdk_ec2.types.resource_arn.ResourceArn"
    ]
    """<p>The Amazon Resource Number (ARN) of the local gateway virtual interface group.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>The tags assigned to the virtual interface group.</p>"""
    configuration_state: NotRequired[
        "aws_sdk_ec2.types.local_gateway_virtual_interface_group_configuration_state.LocalGatewayVirtualInterfaceGroupConfigurationState"
    ]
    """<p>The current state of the local gateway virtual interface group.</p>"""
