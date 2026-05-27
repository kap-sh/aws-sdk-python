"""Generated from Smithy shape ``com.amazonaws.ec2#VpcPeeringConnectionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.vpc_peering_connection

VpcPeeringConnectionList: TypeAlias = list[
    "aws_sdk_ec2.types.vpc_peering_connection.VpcPeeringConnection"
]
