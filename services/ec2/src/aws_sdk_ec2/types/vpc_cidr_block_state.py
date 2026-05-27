"""Generated from Smithy shape ``com.amazonaws.ec2#VpcCidrBlockState``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.vpc_cidr_block_state_code


class VpcCidrBlockState(TypedDict):
    state: NotRequired[
        "aws_sdk_ec2.types.vpc_cidr_block_state_code.VpcCidrBlockStateCode"
    ]
    """<p>The state of the CIDR block.</p>"""
    status_message: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A message about the status of the CIDR block, if applicable.</p>"""
