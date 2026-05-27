"""Generated from Smithy shape ``com.amazonaws.ec2#VpcCidrBlockAssociation``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.vpc_cidr_block_state


class VpcCidrBlockAssociation(TypedDict):
    association_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The association ID for the IPv4 CIDR block.</p>"""
    cidr_block: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The IPv4 CIDR block.</p>"""
    cidr_block_state: NotRequired[
        "aws_sdk_ec2.types.vpc_cidr_block_state.VpcCidrBlockState"
    ]
    """<p>Information about the state of the CIDR block.</p>"""
