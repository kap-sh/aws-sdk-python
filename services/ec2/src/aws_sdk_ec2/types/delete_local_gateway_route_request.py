"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteLocalGatewayRouteRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.local_gateway_routetable_id
    import aws_sdk_ec2.types.prefix_list_resource_id
    import aws_sdk_ec2.types.string


class DeleteLocalGatewayRouteRequest(TypedDict):
    destination_cidr_block: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The CIDR range for the route. This must match the CIDR for the route exactly.</p>"""
    local_gateway_route_table_id: NotRequired[
        "aws_sdk_ec2.types.local_gateway_routetable_id.LocalGatewayRoutetableId"
    ]
    """<p>The ID of the local gateway route table.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    destination_prefix_list_id: NotRequired[
        "aws_sdk_ec2.types.prefix_list_resource_id.PrefixListResourceId"
    ]
    """<p> Use a prefix list in place of <code>DestinationCidrBlock</code>. You cannot use <code>DestinationPrefixListId</code> and <code>DestinationCidrBlock</code> in the same request. </p>"""
