"""Generated from Smithy shape ``com.amazonaws.ec2#CreateLocalGatewayRouteTableVpcAssociationResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.local_gateway_route_table_vpc_association


class CreateLocalGatewayRouteTableVpcAssociationResult(TypedDict):
    local_gateway_route_table_vpc_association: NotRequired[
        "aws_sdk_ec2.types.local_gateway_route_table_vpc_association.LocalGatewayRouteTableVpcAssociation"
    ]
    """<p>Information about the association.</p>"""
