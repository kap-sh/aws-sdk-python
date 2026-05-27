"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteCoipPoolRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.ipv4_pool_coip_id


class DeleteCoipPoolRequest(TypedDict):
    coip_pool_id: NotRequired["aws_sdk_ec2.types.ipv4_pool_coip_id.Ipv4PoolCoipId"]
    """<p>The ID of the CoIP pool that you want to delete. </p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
