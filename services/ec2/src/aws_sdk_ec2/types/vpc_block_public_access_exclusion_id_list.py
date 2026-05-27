"""Generated from Smithy shape ``com.amazonaws.ec2#VpcBlockPublicAccessExclusionIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.vpc_block_public_access_exclusion_id

VpcBlockPublicAccessExclusionIdList: TypeAlias = list[
    "aws_sdk_ec2.types.vpc_block_public_access_exclusion_id.VpcBlockPublicAccessExclusionId"
]
