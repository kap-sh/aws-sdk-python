"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeVpcBlockPublicAccessOptionsResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.vpc_block_public_access_options


class DescribeVpcBlockPublicAccessOptionsResult(TypedDict):
    vpc_block_public_access_options: NotRequired[
        "aws_sdk_ec2.types.vpc_block_public_access_options.VpcBlockPublicAccessOptions"
    ]
    """<p>Details related to the options.</p>"""
