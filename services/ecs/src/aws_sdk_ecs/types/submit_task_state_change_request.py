"""Generated from Smithy shape ``com.amazonaws.ecs#SubmitTaskStateChangeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ecs.types.attachment_state_changes
    import aws_sdk_ecs.types.container_state_changes
    import aws_sdk_ecs.types.managed_agent_state_changes
    import aws_sdk_ecs.types.string
    import aws_sdk_ecs.types.timestamp


class SubmitTaskStateChangeRequest(TypedDict, closed=True):
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


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SubmitTaskStateChangeRequest) -> dict:
    out: dict = {}
    if "cluster" in value:
        out["cluster"] = value["cluster"]
    if "task" in value:
        out["task"] = value["task"]
    if "status" in value:
        out["status"] = value["status"]
    if "reason" in value:
        out["reason"] = value["reason"]
    if "containers" in value:
        import aws_sdk_ecs.types.container_state_changes

        out["containers"] = (
            aws_sdk_ecs.types.container_state_changes.serialize_aws_json_1_1(
                value["containers"]
            )
        )
    if "attachments" in value:
        import aws_sdk_ecs.types.attachment_state_changes

        out["attachments"] = (
            aws_sdk_ecs.types.attachment_state_changes.serialize_aws_json_1_1(
                value["attachments"]
            )
        )
    if "managed_agents" in value:
        import aws_sdk_ecs.types.managed_agent_state_changes

        out["managedAgents"] = (
            aws_sdk_ecs.types.managed_agent_state_changes.serialize_aws_json_1_1(
                value["managed_agents"]
            )
        )
    if "pull_started_at" in value:
        import aws_sdk_ecs.types.timestamp

        out["pullStartedAt"] = aws_sdk_ecs.types.timestamp.serialize_aws_json_1_1(
            value["pull_started_at"]
        )
    if "pull_stopped_at" in value:
        import aws_sdk_ecs.types.timestamp

        out["pullStoppedAt"] = aws_sdk_ecs.types.timestamp.serialize_aws_json_1_1(
            value["pull_stopped_at"]
        )
    if "execution_stopped_at" in value:
        import aws_sdk_ecs.types.timestamp

        out["executionStoppedAt"] = aws_sdk_ecs.types.timestamp.serialize_aws_json_1_1(
            value["execution_stopped_at"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SubmitTaskStateChangeRequest:
    out: SubmitTaskStateChangeRequest = {}  # type: ignore[typeddict-item]
    if "cluster" in data:
        out["cluster"] = data["cluster"]
    if "task" in data:
        out["task"] = data["task"]
    if "status" in data:
        out["status"] = data["status"]
    if "reason" in data:
        out["reason"] = data["reason"]
    if "containers" in data:
        import aws_sdk_ecs.types.container_state_changes

        out["containers"] = (
            aws_sdk_ecs.types.container_state_changes.deserialize_aws_json_1_1(
                data["containers"]
            )
        )
    if "attachments" in data:
        import aws_sdk_ecs.types.attachment_state_changes

        out["attachments"] = (
            aws_sdk_ecs.types.attachment_state_changes.deserialize_aws_json_1_1(
                data["attachments"]
            )
        )
    if "managedAgents" in data:
        import aws_sdk_ecs.types.managed_agent_state_changes

        out["managed_agents"] = (
            aws_sdk_ecs.types.managed_agent_state_changes.deserialize_aws_json_1_1(
                data["managedAgents"]
            )
        )
    if "pullStartedAt" in data:
        import aws_sdk_ecs.types.timestamp

        out["pull_started_at"] = aws_sdk_ecs.types.timestamp.deserialize_aws_json_1_1(
            data["pullStartedAt"]
        )
    if "pullStoppedAt" in data:
        import aws_sdk_ecs.types.timestamp

        out["pull_stopped_at"] = aws_sdk_ecs.types.timestamp.deserialize_aws_json_1_1(
            data["pullStoppedAt"]
        )
    if "executionStoppedAt" in data:
        import aws_sdk_ecs.types.timestamp

        out["execution_stopped_at"] = (
            aws_sdk_ecs.types.timestamp.deserialize_aws_json_1_1(
                data["executionStoppedAt"]
            )
        )
    return out
