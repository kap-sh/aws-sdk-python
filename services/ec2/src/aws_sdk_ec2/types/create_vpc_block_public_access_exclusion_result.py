"""Generated from Smithy shape ``com.amazonaws.ec2#CreateVpcBlockPublicAccessExclusionResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.vpc_block_public_access_exclusion


class CreateVpcBlockPublicAccessExclusionResult(TypedDict):
    vpc_block_public_access_exclusion: NotRequired[
        "aws_sdk_ec2.types.vpc_block_public_access_exclusion.VpcBlockPublicAccessExclusion"
    ]
    """<p>Details about an exclusion.</p>"""
