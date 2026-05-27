"""Generated from Smithy shape ``com.amazonaws.ec2#CoipPoolSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.coip_pool

CoipPoolSet: TypeAlias = list["aws_sdk_ec2.types.coip_pool.CoipPool"]
