"""Generated from Smithy shape ``com.amazonaws.ec2#UserIdGroupPairSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.user_id_group_pair

UserIdGroupPairSet: TypeAlias = list[
    "aws_sdk_ec2.types.user_id_group_pair.UserIdGroupPair"
]
