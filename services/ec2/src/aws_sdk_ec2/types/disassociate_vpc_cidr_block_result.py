"""Generated from Smithy shape ``com.amazonaws.ec2#DisassociateVpcCidrBlockResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.vpc_cidr_block_association
    import aws_sdk_ec2.types.vpc_ipv6_cidr_block_association


class DisassociateVpcCidrBlockResult(TypedDict):
    ipv6_cidr_block_association: NotRequired[
        "aws_sdk_ec2.types.vpc_ipv6_cidr_block_association.VpcIpv6CidrBlockAssociation"
    ]
    """<p>Information about the IPv6 CIDR block association.</p>"""
    cidr_block_association: NotRequired[
        "aws_sdk_ec2.types.vpc_cidr_block_association.VpcCidrBlockAssociation"
    ]
    """<p>Information about the IPv4 CIDR block association.</p>"""
    vpc_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the VPC.</p>"""
