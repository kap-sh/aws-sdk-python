"""Generated from Smithy shape ``com.amazonaws.ec2#EnableAddressTransferRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.allocation_id
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.string


class EnableAddressTransferRequest(TypedDict):
    allocation_id: NotRequired["aws_sdk_ec2.types.allocation_id.AllocationId"]
    """<p>The allocation ID of an Elastic IP address.</p>"""
    transfer_account_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the account that you want to transfer the Elastic IP address to.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
