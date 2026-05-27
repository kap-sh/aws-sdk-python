"""Generated from Smithy shape ``com.amazonaws.ec2#CoipPoolIdSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipv4_pool_coip_id

CoipPoolIdSet: TypeAlias = list["aws_sdk_ec2.types.ipv4_pool_coip_id.Ipv4PoolCoipId"]
