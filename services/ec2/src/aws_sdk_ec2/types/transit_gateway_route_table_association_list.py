"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayRouteTableAssociationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.transit_gateway_route_table_association

TransitGatewayRouteTableAssociationList: TypeAlias = list[
    "aws_sdk_ec2.types.transit_gateway_route_table_association.TransitGatewayRouteTableAssociation"
]
