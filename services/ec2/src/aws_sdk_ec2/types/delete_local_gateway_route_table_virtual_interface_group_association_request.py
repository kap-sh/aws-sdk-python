"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteLocalGatewayRouteTableVirtualInterfaceGroupAssociationRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.local_gateway_route_table_virtual_interface_group_association_id


class DeleteLocalGatewayRouteTableVirtualInterfaceGroupAssociationRequest(TypedDict):
    local_gateway_route_table_virtual_interface_group_association_id: NotRequired[
        "aws_sdk_ec2.types.local_gateway_route_table_virtual_interface_group_association_id.LocalGatewayRouteTableVirtualInterfaceGroupAssociationId"
    ]
    """<p> The ID of the local gateway route table virtual interface group association. </p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
