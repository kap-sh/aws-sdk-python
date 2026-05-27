"""Generated from Smithy shape ``com.amazonaws.ec2#DeprovisionIpamPoolCidrRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.ipam_pool_id
    import aws_sdk_ec2.types.string


class DeprovisionIpamPoolCidrRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>A check for whether you have the required permissions for the action without actually making the request and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    ipam_pool_id: NotRequired["aws_sdk_ec2.types.ipam_pool_id.IpamPoolId"]
    """<p>The ID of the pool that has the CIDR you want to deprovision.</p>"""
    cidr: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The CIDR which you want to deprovision from the pool.</p>"""
