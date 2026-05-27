"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteIpamExternalResourceVerificationTokenResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipam_external_resource_verification_token


class DeleteIpamExternalResourceVerificationTokenResult(TypedDict):
    ipam_external_resource_verification_token: NotRequired[
        "aws_sdk_ec2.types.ipam_external_resource_verification_token.IpamExternalResourceVerificationToken"
    ]
    """<p>The verification token.</p>"""
