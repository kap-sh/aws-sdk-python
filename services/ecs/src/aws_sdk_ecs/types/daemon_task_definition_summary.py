"""Generated from Smithy shape ``com.amazonaws.ecs#DaemonTaskDefinitionSummary``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.daemon_task_definition_status
    import aws_sdk_ecs.types.string
    import aws_sdk_ecs.types.timestamp


class DaemonTaskDefinitionSummary(TypedDict):
    arn: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the daemon task definition.</p>"""
    registered_at: NotRequired["aws_sdk_ecs.types.timestamp.Timestamp"]
    """<p>The Unix timestamp for the time when the daemon task definition was registered.</p>"""
    registered_by: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The principal that registered the daemon task definition.</p>"""
    delete_requested_at: NotRequired["aws_sdk_ecs.types.timestamp.Timestamp"]
    """<p>The Unix timestamp for the time when the daemon task definition delete was requested.</p>"""
    status: NotRequired[
        "aws_sdk_ecs.types.daemon_task_definition_status.DaemonTaskDefinitionStatus"
    ]
    """<p>The status of the daemon task definition.</p>"""
