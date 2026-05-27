"""Generated from Smithy shape ``com.amazonaws.ec2#CancelImportTaskRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.import_task_id
    import aws_sdk_ec2.types.string


class CancelImportTaskRequest(TypedDict):
    cancel_reason: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The reason for canceling the task.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    import_task_id: NotRequired["aws_sdk_ec2.types.import_task_id.ImportTaskId"]
    """<p>The ID of the import image or import snapshot task to be canceled.</p>"""
