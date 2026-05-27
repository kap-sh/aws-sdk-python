"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteVerifiedAccessTrustProviderResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.verified_access_trust_provider


class DeleteVerifiedAccessTrustProviderResult(TypedDict):
    verified_access_trust_provider: NotRequired[
        "aws_sdk_ec2.types.verified_access_trust_provider.VerifiedAccessTrustProvider"
    ]
    """<p>Details about the Verified Access trust provider.</p>"""
