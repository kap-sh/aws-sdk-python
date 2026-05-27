"""Generated from Smithy shape ``com.amazonaws.ec2#PoolCidrBlocksSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.pool_cidr_block

PoolCidrBlocksSet: TypeAlias = list["aws_sdk_ec2.types.pool_cidr_block.PoolCidrBlock"]
