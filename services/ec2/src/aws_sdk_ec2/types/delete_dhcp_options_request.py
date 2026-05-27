"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteDhcpOptionsRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.dhcp_options_id


class DeleteDhcpOptionsRequest(TypedDict):
    dhcp_options_id: NotRequired["aws_sdk_ec2.types.dhcp_options_id.DhcpOptionsId"]
    """<p>The ID of the DHCP options set.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
