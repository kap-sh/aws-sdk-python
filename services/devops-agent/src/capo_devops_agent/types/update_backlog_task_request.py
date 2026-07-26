"""Generated from Smithy shape ``com.amazonaws.devopsagent#UpdateBacklogTaskRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_devops_agent.types.agent_space_id
    import capo_devops_agent.types.resource_id
    import capo_devops_agent.types.task_status


class UpdateBacklogTaskRequest(TypedDict, closed=True):
    agent_space_id: "capo_devops_agent.types.agent_space_id.AgentSpaceId"
    """<p>The unique identifier for the agent space containing the task</p>"""
    task_id: "capo_devops_agent.types.resource_id.ResourceId"
    """<p>The unique identifier of the task to update</p>"""
    task_status: NotRequired["capo_devops_agent.types.task_status.TaskStatus"]
    """<p>Updated task status</p>"""
    client_token: NotRequired["str"]
    """<p>Client-provided token for idempotent operations</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateBacklogTaskRequest) -> dict:
    out: dict = {}
    if "task_status" in value:
        import capo_devops_agent.types.task_status

        out["taskStatus"] = capo_devops_agent.types.task_status.serialize_json(
            value["task_status"]
        )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> UpdateBacklogTaskRequest:
    out: UpdateBacklogTaskRequest = {}  # type: ignore[typeddict-item]
    if "taskStatus" in data:
        import capo_devops_agent.types.task_status

        out["task_status"] = capo_devops_agent.types.task_status.deserialize_json(
            data["taskStatus"]
        )
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
