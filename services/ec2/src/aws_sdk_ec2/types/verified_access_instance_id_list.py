"""Generated from Smithy shape ``com.amazonaws.ec2#VerifiedAccessInstanceIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.verified_access_instance_id

VerifiedAccessInstanceIdList: TypeAlias = list[
    "aws_sdk_ec2.types.verified_access_instance_id.VerifiedAccessInstanceId"
]
