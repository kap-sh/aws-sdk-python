"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyVerifiedAccessEndpointLoadBalancerOptions``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.modify_verified_access_endpoint_port_range_list
    import aws_sdk_ec2.types.modify_verified_access_endpoint_subnet_id_list
    import aws_sdk_ec2.types.verified_access_endpoint_port_number
    import aws_sdk_ec2.types.verified_access_endpoint_protocol


class ModifyVerifiedAccessEndpointLoadBalancerOptions(TypedDict):
    subnet_ids: NotRequired[
        "aws_sdk_ec2.types.modify_verified_access_endpoint_subnet_id_list.ModifyVerifiedAccessEndpointSubnetIdList"
    ]
    """<p>The IDs of the subnets.</p>"""
    protocol: NotRequired[
        "aws_sdk_ec2.types.verified_access_endpoint_protocol.VerifiedAccessEndpointProtocol"
    ]
    """<p>The IP protocol.</p>"""
    port: NotRequired[
        "aws_sdk_ec2.types.verified_access_endpoint_port_number.VerifiedAccessEndpointPortNumber"
    ]
    """<p>The IP port number.</p>"""
    port_ranges: NotRequired[
        "aws_sdk_ec2.types.modify_verified_access_endpoint_port_range_list.ModifyVerifiedAccessEndpointPortRangeList"
    ]
    """<p>The port ranges.</p>"""
