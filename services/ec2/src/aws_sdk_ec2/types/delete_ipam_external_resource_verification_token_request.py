"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteIpamExternalResourceVerificationTokenRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.ipam_external_resource_verification_token_id


class DeleteIpamExternalResourceVerificationTokenRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>A check for whether you have the required permissions for the action without actually making the request and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    ipam_external_resource_verification_token_id: NotRequired[
        "aws_sdk_ec2.types.ipam_external_resource_verification_token_id.IpamExternalResourceVerificationTokenId"
    ]
    """<p>The token ID.</p>"""
