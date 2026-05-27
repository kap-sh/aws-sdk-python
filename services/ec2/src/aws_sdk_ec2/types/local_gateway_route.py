"""Generated from Smithy shape ``com.amazonaws.ec2#LocalGatewayRoute``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.coip_pool_id
    import aws_sdk_ec2.types.local_gateway_route_state
    import aws_sdk_ec2.types.local_gateway_route_type
    import aws_sdk_ec2.types.local_gateway_routetable_id
    import aws_sdk_ec2.types.local_gateway_virtual_interface_group_id
    import aws_sdk_ec2.types.network_interface_id
    import aws_sdk_ec2.types.prefix_list_resource_id
    import aws_sdk_ec2.types.resource_arn
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.subnet_id


class LocalGatewayRoute(TypedDict):
    destination_cidr_block: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The CIDR block used for destination matches.</p>"""
    local_gateway_virtual_interface_group_id: NotRequired[
        "aws_sdk_ec2.types.local_gateway_virtual_interface_group_id.LocalGatewayVirtualInterfaceGroupId"
    ]
    """<p>The ID of the virtual interface group.</p>"""
    type: NotRequired[
        "aws_sdk_ec2.types.local_gateway_route_type.LocalGatewayRouteType"
    ]
    """<p>The route type.</p>"""
    state: NotRequired[
        "aws_sdk_ec2.types.local_gateway_route_state.LocalGatewayRouteState"
    ]
    """<p>The state of the route.</p>"""
    local_gateway_route_table_id: NotRequired[
        "aws_sdk_ec2.types.local_gateway_routetable_id.LocalGatewayRoutetableId"
    ]
    """<p>The ID of the local gateway route table.</p>"""
    local_gateway_route_table_arn: NotRequired[
        "aws_sdk_ec2.types.resource_arn.ResourceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the local gateway route table.</p>"""
    owner_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Amazon Web Services account that owns the local gateway route.</p>"""
    subnet_id: NotRequired["aws_sdk_ec2.types.subnet_id.SubnetId"]
    """<p>The ID of the subnet.</p>"""
    coip_pool_id: NotRequired["aws_sdk_ec2.types.coip_pool_id.CoipPoolId"]
    """<p>The ID of the customer-owned address pool.</p>"""
    network_interface_id: NotRequired[
        "aws_sdk_ec2.types.network_interface_id.NetworkInterfaceId"
    ]
    """<p>The ID of the network interface.</p>"""
    destination_prefix_list_id: NotRequired[
        "aws_sdk_ec2.types.prefix_list_resource_id.PrefixListResourceId"
    ]
    """<p> The ID of the prefix list. </p>"""
