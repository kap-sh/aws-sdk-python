"""Generated from Smithy shape ``com.amazonaws.ec2#CreateLocalGatewayRouteTableRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.local_gateway_id
    import aws_sdk_ec2.types.local_gateway_route_table_mode
    import aws_sdk_ec2.types.tag_specification_list


class CreateLocalGatewayRouteTableRequest(TypedDict):
    local_gateway_id: NotRequired["aws_sdk_ec2.types.local_gateway_id.LocalGatewayId"]
    """<p> The ID of the local gateway. </p>"""
    mode: NotRequired[
        "aws_sdk_ec2.types.local_gateway_route_table_mode.LocalGatewayRouteTableMode"
    ]
    """<p> The mode of the local gateway route table. </p>"""
    tag_specifications: NotRequired[
        "aws_sdk_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p> The tags assigned to the local gateway route table. </p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
