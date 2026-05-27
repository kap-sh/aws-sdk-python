"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteIpamPoolRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.ipam_pool_id


class DeleteIpamPoolRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>A check for whether you have the required permissions for the action without actually making the request and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    ipam_pool_id: NotRequired["aws_sdk_ec2.types.ipam_pool_id.IpamPoolId"]
    """<p>The ID of the pool to delete.</p>"""
    cascade: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Enables you to quickly delete an IPAM pool and all resources within that pool, including provisioned CIDRs, allocations, and other pools.</p> <important> <p>You can only use this option to delete pools in the private scope or pools in the public scope with a source resource. A source resource is a resource used to provision CIDRs to a resource planning pool.</p> </important>"""
