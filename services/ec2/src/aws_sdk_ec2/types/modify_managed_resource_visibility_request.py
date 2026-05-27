"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyManagedResourceVisibilityRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.managed_resource_default_visibility


class ModifyManagedResourceVisibilityRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the operation, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    default_visibility: NotRequired[
        "aws_sdk_ec2.types.managed_resource_default_visibility.ManagedResourceDefaultVisibility"
    ]
    """<p>The default visibility setting for managed resources. Valid values: <code>hidden</code> | <code>visible</code>.</p>"""
