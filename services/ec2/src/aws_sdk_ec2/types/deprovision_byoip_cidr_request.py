"""Generated from Smithy shape ``com.amazonaws.ec2#DeprovisionByoipCidrRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.string


class DeprovisionByoipCidrRequest(TypedDict):
    cidr: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The address range, in CIDR notation. The prefix must be the same prefix that you specified when you provisioned the address range.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
