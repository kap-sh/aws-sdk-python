"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyIpamPoolAllocationRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.ipam_pool_allocation_id
    import aws_sdk_ec2.types.string


class ModifyIpamPoolAllocationRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>A check for whether you have the required permissions for the action without actually making the request and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    ipam_pool_allocation_id: NotRequired[
        "aws_sdk_ec2.types.ipam_pool_allocation_id.IpamPoolAllocationId"
    ]
    """<p>The ID of the IPAM pool allocation you want to modify.</p>"""
    description: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The new description for the IPAM pool allocation. If you submit a <code>null</code> value, the description is removed from the allocation.</p>"""
