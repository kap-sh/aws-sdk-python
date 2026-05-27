"""Generated from Smithy shape ``com.amazonaws.ec2#ProvisionIpamByoasnRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.asn_authorization_context
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.ipam_id
    import aws_sdk_ec2.types.string


class ProvisionIpamByoasnRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    ipam_id: NotRequired["aws_sdk_ec2.types.ipam_id.IpamId"]
    """<p>An IPAM ID.</p>"""
    asn: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A public 2-byte or 4-byte ASN.</p>"""
    asn_authorization_context: NotRequired[
        "aws_sdk_ec2.types.asn_authorization_context.AsnAuthorizationContext"
    ]
    """<p>An ASN authorization context.</p>"""
