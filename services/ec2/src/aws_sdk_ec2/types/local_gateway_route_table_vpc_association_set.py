"""Generated from Smithy shape ``com.amazonaws.ec2#LocalGatewayRouteTableVpcAssociationSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.local_gateway_route_table_vpc_association

LocalGatewayRouteTableVpcAssociationSet: TypeAlias = list[
    "aws_sdk_ec2.types.local_gateway_route_table_vpc_association.LocalGatewayRouteTableVpcAssociation"
]
