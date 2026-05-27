"""Generated from Smithy shape ``com.amazonaws.ec2#ReleaseIpamPoolAllocationRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.ipam_pool_allocation_id
    import aws_sdk_ec2.types.ipam_pool_id
    import aws_sdk_ec2.types.string


class ReleaseIpamPoolAllocationRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>A check for whether you have the required permissions for the action without actually making the request and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    ipam_pool_id: NotRequired["aws_sdk_ec2.types.ipam_pool_id.IpamPoolId"]
    """<p>The ID of the IPAM pool which contains the allocation you want to release.</p>"""
    cidr: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The CIDR of the allocation you want to release.</p>"""
    ipam_pool_allocation_id: NotRequired[
        "aws_sdk_ec2.types.ipam_pool_allocation_id.IpamPoolAllocationId"
    ]
    """<p>The ID of the allocation.</p>"""
