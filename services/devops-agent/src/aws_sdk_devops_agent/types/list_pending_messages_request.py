"""Generated from Smithy shape ``com.amazonaws.devopsagent#ListPendingMessagesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_devops_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_devops_agent.types.agent_space_id
    import aws_sdk_devops_agent.types.resource_id


class ListPendingMessagesRequest(TypedDict):
    agent_space_id: "aws_sdk_devops_agent.types.agent_space_id.AgentSpaceId"
    execution_id: "aws_sdk_devops_agent.types.resource_id.ResourceId"
    """<p>The unique identifier of the execution whose journal records to retrieve</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPendingMessagesRequest) -> dict:
    out: dict = {}
    out["executionId"] = value["execution_id"]
    return out


def deserialize_json(data: dict) -> ListPendingMessagesRequest:
    out: ListPendingMessagesRequest = {}  # type: ignore[typeddict-item]
    if "executionId" in data:
        out["execution_id"] = data["executionId"]
    else:
        raise DeserializationError("ListPendingMessagesRequest.execution_id required")
    return out
