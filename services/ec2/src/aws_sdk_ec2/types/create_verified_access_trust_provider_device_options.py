"""Generated from Smithy shape ``com.amazonaws.ec2#CreateVerifiedAccessTrustProviderDeviceOptions``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class CreateVerifiedAccessTrustProviderDeviceOptions(TypedDict):
    tenant_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the tenant application with the device-identity provider.</p>"""
    public_signing_key_url: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p> The URL Amazon Web Services Verified Access will use to verify the authenticity of the device tokens. </p>"""
