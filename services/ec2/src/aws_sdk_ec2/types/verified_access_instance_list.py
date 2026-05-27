"""Generated from Smithy shape ``com.amazonaws.ec2#VerifiedAccessInstanceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.verified_access_instance

VerifiedAccessInstanceList: TypeAlias = list[
    "aws_sdk_ec2.types.verified_access_instance.VerifiedAccessInstance"
]
