"""Generated from Smithy shape ``com.amazonaws.ec2#RouteServerEndpoint``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.network_interface_id
    import aws_sdk_ec2.types.route_server_endpoint_id
    import aws_sdk_ec2.types.route_server_endpoint_state
    import aws_sdk_ec2.types.route_server_id
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.subnet_id
    import aws_sdk_ec2.types.tag_list
    import aws_sdk_ec2.types.vpc_id


class RouteServerEndpoint(TypedDict):
    route_server_id: NotRequired["aws_sdk_ec2.types.route_server_id.RouteServerId"]
    """<p>The ID of the route server associated with this endpoint.</p>"""
    route_server_endpoint_id: NotRequired[
        "aws_sdk_ec2.types.route_server_endpoint_id.RouteServerEndpointId"
    ]
    """<p>The unique identifier of the route server endpoint.</p>"""
    vpc_id: NotRequired["aws_sdk_ec2.types.vpc_id.VpcId"]
    """<p>The ID of the VPC containing the endpoint.</p>"""
    subnet_id: NotRequired["aws_sdk_ec2.types.subnet_id.SubnetId"]
    """<p>The ID of the subnet to place the route server endpoint into.</p>"""
    eni_id: NotRequired["aws_sdk_ec2.types.network_interface_id.NetworkInterfaceId"]
    """<p>The ID of the Elastic network interface for the endpoint.</p>"""
    eni_address: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The IP address of the Elastic network interface for the endpoint.</p>"""
    state: NotRequired[
        "aws_sdk_ec2.types.route_server_endpoint_state.RouteServerEndpointState"
    ]
    """<p>The current state of the route server endpoint.</p>"""
    failure_reason: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The reason for any failure in endpoint creation or operation.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>Any tags assigned to the route server endpoint.</p>"""
