"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyAddressAttributeRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.allocation_id
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.string


class ModifyAddressAttributeRequest(TypedDict):
    allocation_id: NotRequired["aws_sdk_ec2.types.allocation_id.AllocationId"]
    """<p>[EC2-VPC] The allocation ID.</p>"""
    domain_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The domain name to modify for the IP address.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
