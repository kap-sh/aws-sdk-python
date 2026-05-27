"""Generated from Smithy shape ``com.amazonaws.ec2#CreateCoipCidrRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.ipv4_pool_coip_id
    import aws_sdk_ec2.types.string


class CreateCoipCidrRequest(TypedDict):
    cidr: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p> A customer-owned IP address range to create. </p>"""
    coip_pool_id: NotRequired["aws_sdk_ec2.types.ipv4_pool_coip_id.Ipv4PoolCoipId"]
    """<p> The ID of the address pool. </p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
