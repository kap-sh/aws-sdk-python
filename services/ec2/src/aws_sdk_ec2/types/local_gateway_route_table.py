"""Generated from Smithy shape ``com.amazonaws.ec2#LocalGatewayRouteTable``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.local_gateway_id
    import aws_sdk_ec2.types.local_gateway_route_table_mode
    import aws_sdk_ec2.types.resource_arn
    import aws_sdk_ec2.types.state_reason
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list


class LocalGatewayRouteTable(TypedDict):
    local_gateway_route_table_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the local gateway route table.</p>"""
    local_gateway_route_table_arn: NotRequired[
        "aws_sdk_ec2.types.resource_arn.ResourceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the local gateway route table.</p>"""
    local_gateway_id: NotRequired["aws_sdk_ec2.types.local_gateway_id.LocalGatewayId"]
    """<p>The ID of the local gateway.</p>"""
    outpost_arn: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the Outpost.</p>"""
    owner_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Amazon Web Services account that owns the local gateway route table.</p>"""
    state: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The state of the local gateway route table.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>The tags assigned to the local gateway route table.</p>"""
    mode: NotRequired[
        "aws_sdk_ec2.types.local_gateway_route_table_mode.LocalGatewayRouteTableMode"
    ]
    """<p>The mode of the local gateway route table.</p>"""
    state_reason: NotRequired["aws_sdk_ec2.types.state_reason.StateReason"]
    """<p>Information about the state change.</p>"""
