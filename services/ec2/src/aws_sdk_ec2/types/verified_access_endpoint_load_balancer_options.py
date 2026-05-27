"""Generated from Smithy shape ``com.amazonaws.ec2#VerifiedAccessEndpointLoadBalancerOptions``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.verified_access_endpoint_port_number
    import aws_sdk_ec2.types.verified_access_endpoint_port_range_list
    import aws_sdk_ec2.types.verified_access_endpoint_protocol
    import aws_sdk_ec2.types.verified_access_endpoint_subnet_id_list


class VerifiedAccessEndpointLoadBalancerOptions(TypedDict):
    protocol: NotRequired[
        "aws_sdk_ec2.types.verified_access_endpoint_protocol.VerifiedAccessEndpointProtocol"
    ]
    """<p>The IP protocol.</p>"""
    port: NotRequired[
        "aws_sdk_ec2.types.verified_access_endpoint_port_number.VerifiedAccessEndpointPortNumber"
    ]
    """<p>The IP port number.</p>"""
    load_balancer_arn: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ARN of the load balancer.</p>"""
    subnet_ids: NotRequired[
        "aws_sdk_ec2.types.verified_access_endpoint_subnet_id_list.VerifiedAccessEndpointSubnetIdList"
    ]
    """<p>The IDs of the subnets.</p>"""
    port_ranges: NotRequired[
        "aws_sdk_ec2.types.verified_access_endpoint_port_range_list.VerifiedAccessEndpointPortRangeList"
    ]
    """<p>The port ranges.</p>"""
