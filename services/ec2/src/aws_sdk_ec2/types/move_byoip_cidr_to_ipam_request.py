"""Generated from Smithy shape ``com.amazonaws.ec2#MoveByoipCidrToIpamRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.ipam_pool_id
    import aws_sdk_ec2.types.string


class MoveByoipCidrToIpamRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>A check for whether you have the required permissions for the action without actually making the request and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    cidr: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The BYOIP CIDR.</p>"""
    ipam_pool_id: NotRequired["aws_sdk_ec2.types.ipam_pool_id.IpamPoolId"]
    """<p>The IPAM pool ID.</p>"""
    ipam_pool_owner: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Amazon Web Services account ID of the owner of the IPAM pool.</p>"""
