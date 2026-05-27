"""Generated from Smithy shape ``com.amazonaws.ec2#VerifiedAccessEndpointCidrOptions``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.verified_access_endpoint_port_range_list
    import aws_sdk_ec2.types.verified_access_endpoint_protocol
    import aws_sdk_ec2.types.verified_access_endpoint_subnet_id_list


class VerifiedAccessEndpointCidrOptions(TypedDict):
    cidr: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The CIDR.</p>"""
    port_ranges: NotRequired[
        "aws_sdk_ec2.types.verified_access_endpoint_port_range_list.VerifiedAccessEndpointPortRangeList"
    ]
    """<p>The port ranges.</p>"""
    protocol: NotRequired[
        "aws_sdk_ec2.types.verified_access_endpoint_protocol.VerifiedAccessEndpointProtocol"
    ]
    """<p>The protocol.</p>"""
    subnet_ids: NotRequired[
        "aws_sdk_ec2.types.verified_access_endpoint_subnet_id_list.VerifiedAccessEndpointSubnetIdList"
    ]
    """<p>The IDs of the subnets.</p>"""
