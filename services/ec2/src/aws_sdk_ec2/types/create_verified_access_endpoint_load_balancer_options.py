"""Generated from Smithy shape ``com.amazonaws.ec2#CreateVerifiedAccessEndpointLoadBalancerOptions``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.create_verified_access_endpoint_port_range_list
    import aws_sdk_ec2.types.create_verified_access_endpoint_subnet_id_list
    import aws_sdk_ec2.types.load_balancer_arn
    import aws_sdk_ec2.types.verified_access_endpoint_port_number
    import aws_sdk_ec2.types.verified_access_endpoint_protocol


class CreateVerifiedAccessEndpointLoadBalancerOptions(TypedDict):
    protocol: NotRequired[
        "aws_sdk_ec2.types.verified_access_endpoint_protocol.VerifiedAccessEndpointProtocol"
    ]
    """<p>The IP protocol.</p>"""
    port: NotRequired[
        "aws_sdk_ec2.types.verified_access_endpoint_port_number.VerifiedAccessEndpointPortNumber"
    ]
    """<p>The IP port number.</p>"""
    load_balancer_arn: NotRequired[
        "aws_sdk_ec2.types.load_balancer_arn.LoadBalancerArn"
    ]
    """<p>The ARN of the load balancer.</p>"""
    subnet_ids: NotRequired[
        "aws_sdk_ec2.types.create_verified_access_endpoint_subnet_id_list.CreateVerifiedAccessEndpointSubnetIdList"
    ]
    """<p>The IDs of the subnets. You can specify only one subnet per Availability Zone.</p>"""
    port_ranges: NotRequired[
        "aws_sdk_ec2.types.create_verified_access_endpoint_port_range_list.CreateVerifiedAccessEndpointPortRangeList"
    ]
    """<p>The port ranges.</p>"""
