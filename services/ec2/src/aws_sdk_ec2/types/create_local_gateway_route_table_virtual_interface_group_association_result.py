"""Generated from Smithy shape ``com.amazonaws.ec2#CreateLocalGatewayRouteTableVirtualInterfaceGroupAssociationResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.local_gateway_route_table_virtual_interface_group_association


class CreateLocalGatewayRouteTableVirtualInterfaceGroupAssociationResult(TypedDict):
    local_gateway_route_table_virtual_interface_group_association: NotRequired[
        "aws_sdk_ec2.types.local_gateway_route_table_virtual_interface_group_association.LocalGatewayRouteTableVirtualInterfaceGroupAssociation"
    ]
    """<p>Information about the local gateway route table virtual interface group association.</p>"""
