"""Generated from Smithy shape ``com.amazonaws.ec2#VpcPeeringConnectionIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.vpc_peering_connection_id

VpcPeeringConnectionIdList: TypeAlias = list[
    "aws_sdk_ec2.types.vpc_peering_connection_id.VpcPeeringConnectionId"
]
