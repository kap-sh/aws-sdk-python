"""Generated from Smithy shape ``com.amazonaws.ec2#VerifiedAccessTrustProviderCondensed``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.device_trust_provider_type
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.trust_provider_type
    import aws_sdk_ec2.types.user_trust_provider_type


class VerifiedAccessTrustProviderCondensed(TypedDict):
    verified_access_trust_provider_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the trust provider.</p>"""
    description: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The description of trust provider.</p>"""
    trust_provider_type: NotRequired[
        "aws_sdk_ec2.types.trust_provider_type.TrustProviderType"
    ]
    """<p>The type of trust provider (user- or device-based).</p>"""
    user_trust_provider_type: NotRequired[
        "aws_sdk_ec2.types.user_trust_provider_type.UserTrustProviderType"
    ]
    """<p>The type of user-based trust provider.</p>"""
    device_trust_provider_type: NotRequired[
        "aws_sdk_ec2.types.device_trust_provider_type.DeviceTrustProviderType"
    ]
    """<p>The type of device-based trust provider.</p>"""
