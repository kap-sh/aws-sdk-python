"""Generated from Smithy shape ``com.amazonaws.ec2#AssociateSubnetCidrBlockResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.subnet_ipv6_cidr_block_association


class AssociateSubnetCidrBlockResult(TypedDict):
    ipv6_cidr_block_association: NotRequired[
        "aws_sdk_ec2.types.subnet_ipv6_cidr_block_association.SubnetIpv6CidrBlockAssociation"
    ]
    """<p>Information about the IPv6 association.</p>"""
    subnet_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the subnet.</p>"""
