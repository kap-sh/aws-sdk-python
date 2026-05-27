"""Generated from Smithy shape ``com.amazonaws.ec2#LocalGatewayRouteTableVirtualInterfaceGroupAssociationIdSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.local_gateway_route_table_virtual_interface_group_association_id

LocalGatewayRouteTableVirtualInterfaceGroupAssociationIdSet: TypeAlias = list[
    "aws_sdk_ec2.types.local_gateway_route_table_virtual_interface_group_association_id.LocalGatewayRouteTableVirtualInterfaceGroupAssociationId"
]
