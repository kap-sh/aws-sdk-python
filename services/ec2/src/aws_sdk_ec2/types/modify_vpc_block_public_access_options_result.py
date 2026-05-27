"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyVpcBlockPublicAccessOptionsResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.vpc_block_public_access_options


class ModifyVpcBlockPublicAccessOptionsResult(TypedDict):
    vpc_block_public_access_options: NotRequired[
        "aws_sdk_ec2.types.vpc_block_public_access_options.VpcBlockPublicAccessOptions"
    ]
    """<p>Details related to the VPC Block Public Access (BPA) options.</p>"""
