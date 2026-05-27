"""Generated from Smithy shape ``com.amazonaws.ecs#DeleteDaemonResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.daemon_status
    import aws_sdk_ecs.types.string
    import aws_sdk_ecs.types.timestamp


class DeleteDaemonResponse(TypedDict):
    daemon_arn: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the daemon.</p>"""
    status: NotRequired["aws_sdk_ecs.types.daemon_status.DaemonStatus"]
    """<p>The status of the daemon. After you call <code>DeleteDaemon</code>, the status changes to <code>DELETE_IN_PROGRESS</code>.</p>"""
    created_at: NotRequired["aws_sdk_ecs.types.timestamp.Timestamp"]
    """<p>The Unix timestamp for the time when the daemon was created.</p>"""
    updated_at: NotRequired["aws_sdk_ecs.types.timestamp.Timestamp"]
    """<p>The Unix timestamp for the time when the daemon was last updated.</p>"""
    deployment_arn: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the daemon deployment that was triggered by the delete operation. This deployment drains existing daemon tasks from the container instances.</p>"""
