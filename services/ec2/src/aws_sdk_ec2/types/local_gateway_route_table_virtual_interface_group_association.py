"""Generated from Smithy shape ``com.amazonaws.ec2#LocalGatewayRouteTableVirtualInterfaceGroupAssociation``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.local_gateway_id
    import aws_sdk_ec2.types.local_gateway_route_table_virtual_interface_group_association_id
    import aws_sdk_ec2.types.local_gateway_virtual_interface_group_id
    import aws_sdk_ec2.types.resource_arn
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list


class LocalGatewayRouteTableVirtualInterfaceGroupAssociation(TypedDict):
    local_gateway_route_table_virtual_interface_group_association_id: NotRequired[
        "aws_sdk_ec2.types.local_gateway_route_table_virtual_interface_group_association_id.LocalGatewayRouteTableVirtualInterfaceGroupAssociationId"
    ]
    """<p>The ID of the association.</p>"""
    local_gateway_virtual_interface_group_id: NotRequired[
        "aws_sdk_ec2.types.local_gateway_virtual_interface_group_id.LocalGatewayVirtualInterfaceGroupId"
    ]
    """<p>The ID of the virtual interface group.</p>"""
    local_gateway_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the local gateway.</p>"""
    local_gateway_route_table_id: NotRequired[
        "aws_sdk_ec2.types.local_gateway_id.LocalGatewayId"
    ]
    """<p>The ID of the local gateway route table.</p>"""
    local_gateway_route_table_arn: NotRequired[
        "aws_sdk_ec2.types.resource_arn.ResourceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the local gateway route table for the virtual interface group.</p>"""
    owner_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Amazon Web Services account that owns the local gateway virtual interface group association.</p>"""
    state: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The state of the association.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>The tags assigned to the association.</p>"""
