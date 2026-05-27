"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteVpnConcentratorRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.vpn_concentrator_id


class DeleteVpnConcentratorRequest(TypedDict):
    vpn_concentrator_id: NotRequired[
        "aws_sdk_ec2.types.vpn_concentrator_id.VpnConcentratorId"
    ]
    """<p>The ID of the VPN concentrator to delete.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
