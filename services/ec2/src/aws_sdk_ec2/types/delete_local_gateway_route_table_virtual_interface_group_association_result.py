"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteLocalGatewayRouteTableVirtualInterfaceGroupAssociationResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.local_gateway_route_table_virtual_interface_group_association


class DeleteLocalGatewayRouteTableVirtualInterfaceGroupAssociationResult(TypedDict):
    local_gateway_route_table_virtual_interface_group_association: NotRequired[
        "aws_sdk_ec2.types.local_gateway_route_table_virtual_interface_group_association.LocalGatewayRouteTableVirtualInterfaceGroupAssociation"
    ]
    """<p>Information about the association.</p>"""
