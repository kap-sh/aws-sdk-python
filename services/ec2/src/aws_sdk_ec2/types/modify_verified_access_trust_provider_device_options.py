"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyVerifiedAccessTrustProviderDeviceOptions``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class ModifyVerifiedAccessTrustProviderDeviceOptions(TypedDict):
    public_signing_key_url: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p> The URL Amazon Web Services Verified Access will use to verify the authenticity of the device tokens.</p>"""
