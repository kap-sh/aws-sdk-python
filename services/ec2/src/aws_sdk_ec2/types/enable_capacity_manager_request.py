"""Generated from Smithy shape ``com.amazonaws.ec2#EnableCapacityManagerRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.string


class EnableCapacityManagerRequest(TypedDict):
    organizations_access: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p> Specifies whether to enable cross-account access for Amazon Web Services Organizations. When enabled, Capacity Manager can aggregate data from all accounts in your organization. Default is false. </p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p> Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>. </p>"""
    client_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p> Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. </p>"""
