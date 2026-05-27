"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteLocalGatewayRouteTableVpcAssociationRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.local_gateway_route_table_vpc_association_id


class DeleteLocalGatewayRouteTableVpcAssociationRequest(TypedDict):
    local_gateway_route_table_vpc_association_id: NotRequired[
        "aws_sdk_ec2.types.local_gateway_route_table_vpc_association_id.LocalGatewayRouteTableVpcAssociationId"
    ]
    """<p>The ID of the association.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
