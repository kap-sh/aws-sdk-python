"""Generated from Smithy shape ``com.amazonaws.ec2#VerifiedAccessEndpointEniOptions``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.network_interface_id
    import aws_sdk_ec2.types.verified_access_endpoint_port_number
    import aws_sdk_ec2.types.verified_access_endpoint_port_range_list
    import aws_sdk_ec2.types.verified_access_endpoint_protocol


class VerifiedAccessEndpointEniOptions(TypedDict):
    network_interface_id: NotRequired[
        "aws_sdk_ec2.types.network_interface_id.NetworkInterfaceId"
    ]
    """<p>The ID of the network interface.</p>"""
    protocol: NotRequired[
        "aws_sdk_ec2.types.verified_access_endpoint_protocol.VerifiedAccessEndpointProtocol"
    ]
    """<p>The IP protocol.</p>"""
    port: NotRequired[
        "aws_sdk_ec2.types.verified_access_endpoint_port_number.VerifiedAccessEndpointPortNumber"
    ]
    """<p>The IP port number.</p>"""
    port_ranges: NotRequired[
        "aws_sdk_ec2.types.verified_access_endpoint_port_range_list.VerifiedAccessEndpointPortRangeList"
    ]
    """<p>The port ranges.</p>"""
