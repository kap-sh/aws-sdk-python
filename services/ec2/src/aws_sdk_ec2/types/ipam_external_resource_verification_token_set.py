"""Generated from Smithy shape ``com.amazonaws.ec2#IpamExternalResourceVerificationTokenSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipam_external_resource_verification_token

IpamExternalResourceVerificationTokenSet: TypeAlias = list[
    "aws_sdk_ec2.types.ipam_external_resource_verification_token.IpamExternalResourceVerificationToken"
]
