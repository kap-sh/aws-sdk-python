"""Generated from Smithy shape ``com.amazonaws.ec2#VerifiedAccessGroupIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.verified_access_group_id

VerifiedAccessGroupIdList: TypeAlias = list[
    "aws_sdk_ec2.types.verified_access_group_id.VerifiedAccessGroupId"
]
