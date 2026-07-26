"""Generated from Smithy shape ``com.amazonaws.devopsagent#GetBacklogTaskRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_devops_agent.types.agent_space_id
    import capo_devops_agent.types.resource_id


class GetBacklogTaskRequest(TypedDict, closed=True):
    agent_space_id: "capo_devops_agent.types.agent_space_id.AgentSpaceId"
    """<p>The unique identifier for the agent space containing the task</p>"""
    task_id: "capo_devops_agent.types.resource_id.ResourceId"
    """<p>The unique identifier of the task to retrieve</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetBacklogTaskRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetBacklogTaskRequest:
    out: GetBacklogTaskRequest = {}  # type: ignore[typeddict-item]
    return out
