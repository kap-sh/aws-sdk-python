"""Generated from Smithy shape ``com.amazonaws.ec2#VpcPeeringConnectionVpcInfo``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.cidr_block_set
    import aws_sdk_ec2.types.ipv6_cidr_block_set
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.vpc_peering_connection_options_description


class VpcPeeringConnectionVpcInfo(TypedDict):
    cidr_block: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The IPv4 CIDR block for the VPC.</p>"""
    ipv6_cidr_block_set: NotRequired[
        "aws_sdk_ec2.types.ipv6_cidr_block_set.Ipv6CidrBlockSet"
    ]
    """<p>The IPv6 CIDR block for the VPC.</p>"""
    cidr_block_set: NotRequired["aws_sdk_ec2.types.cidr_block_set.CidrBlockSet"]
    """<p>Information about the IPv4 CIDR blocks for the VPC.</p>"""
    owner_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Amazon Web Services account that owns the VPC.</p>"""
    peering_options: NotRequired[
        "aws_sdk_ec2.types.vpc_peering_connection_options_description.VpcPeeringConnectionOptionsDescription"
    ]
    """<p>Information about the VPC peering connection options for the accepter or requester VPC.</p>"""
    vpc_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the VPC.</p>"""
    region: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Region in which the VPC is located.</p>"""
