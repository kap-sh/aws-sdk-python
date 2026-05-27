"""Generated from Smithy shape ``com.amazonaws.ecs#SubmitTaskStateChangeRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.attachment_state_changes
    import aws_sdk_ecs.types.container_state_changes
    import aws_sdk_ecs.types.managed_agent_state_changes
    import aws_sdk_ecs.types.string
    import aws_sdk_ecs.types.timestamp


class SubmitTaskStateChangeRequest(TypedDict):
    cluster: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The short name or full Amazon Resource Name (ARN) of the cluster that hosts the task.</p>"""
    task: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The task ID or full ARN of the task in the state change request.</p>"""
    status: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The status of the state change request.</p>"""
    reason: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The reason for the state change request.</p>"""
    containers: NotRequired[
        "aws_sdk_ecs.types.container_state_changes.ContainerStateChanges"
    ]
    """<p>Any containers that's associated with the state change request.</p>"""
    attachments: NotRequired[
        "aws_sdk_ecs.types.attachment_state_changes.AttachmentStateChanges"
    ]
    """<p>Any attachments associated with the state change request.</p>"""
    managed_agents: NotRequired[
        "aws_sdk_ecs.types.managed_agent_state_changes.ManagedAgentStateChanges"
    ]
    """<p>The details for the managed agent that's associated with the task.</p>"""
    pull_started_at: NotRequired["aws_sdk_ecs.types.timestamp.Timestamp"]
    """<p>The Unix timestamp for the time when the container image pull started.</p>"""
    pull_stopped_at: NotRequired["aws_sdk_ecs.types.timestamp.Timestamp"]
    """<p>The Unix timestamp for the time when the container image pull completed.</p>"""
    execution_stopped_at: NotRequired["aws_sdk_ecs.types.timestamp.Timestamp"]
    """<p>The Unix timestamp for the time when the task execution stopped.</p>"""
