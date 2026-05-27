"""Generated from Smithy shape ``com.amazonaws.ec2#AssociateIpamByoasnRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.string


class AssociateIpamByoasnRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    asn: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A public 2-byte or 4-byte ASN.</p>"""
    cidr: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The BYOIP CIDR you want to associate with an ASN.</p>"""
