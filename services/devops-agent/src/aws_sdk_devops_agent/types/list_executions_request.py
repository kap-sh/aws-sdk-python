"""Generated from Smithy shape ``com.amazonaws.devopsagent#ListExecutionsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_devops_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_devops_agent.types.agent_space_id
    import aws_sdk_devops_agent.types.next_token
    import aws_sdk_devops_agent.types.resource_id


class ListExecutionsRequest(TypedDict):
    agent_space_id: "aws_sdk_devops_agent.types.agent_space_id.AgentSpaceId"
    """<p>The unique identifier for the agent space</p>"""
    task_id: "aws_sdk_devops_agent.types.resource_id.ResourceId"
    """<p>The unique identifier of the task whose executions to retrieve</p>"""
    limit: NotRequired["int"]
    """<p>Maximum number of executions to return</p>"""
    next_token: NotRequired["aws_sdk_devops_agent.types.next_token.NextToken"]
    """<p>Token for pagination to retrieve the next set of results</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListExecutionsRequest) -> dict:
    out: dict = {}
    out["taskId"] = value["task_id"]
    if "limit" in value:
        out["limit"] = value["limit"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListExecutionsRequest:
    out: ListExecutionsRequest = {}  # type: ignore[typeddict-item]
    if "taskId" in data:
        out["task_id"] = data["taskId"]
    else:
        raise DeserializationError("ListExecutionsRequest.task_id required")
    if "limit" in data:
        out["limit"] = data["limit"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
