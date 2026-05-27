"""Generated from Smithy shape ``com.amazonaws.ec2#VerifiedAccessTrustProviderCondensedList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.verified_access_trust_provider_condensed

VerifiedAccessTrustProviderCondensedList: TypeAlias = list[
    "aws_sdk_ec2.types.verified_access_trust_provider_condensed.VerifiedAccessTrustProviderCondensed"
]
