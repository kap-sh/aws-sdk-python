"""Generated from Smithy shape ``com.amazonaws.ec2#VerifiedAccessTrustProviderList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.verified_access_trust_provider

VerifiedAccessTrustProviderList: TypeAlias = list[
    "aws_sdk_ec2.types.verified_access_trust_provider.VerifiedAccessTrustProvider"
]
