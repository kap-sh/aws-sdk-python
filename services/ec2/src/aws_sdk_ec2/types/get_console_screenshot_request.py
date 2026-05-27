"""Generated from Smithy shape ``com.amazonaws.ec2#GetConsoleScreenshotRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.instance_id


class GetConsoleScreenshotRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the operation, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    instance_id: NotRequired["aws_sdk_ec2.types.instance_id.InstanceId"]
    """<p>The ID of the instance.</p>"""
    wake_up: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>When set to <code>true</code>, acts as keystroke input and wakes up an instance that's in standby or \"sleep\" mode.</p>"""
