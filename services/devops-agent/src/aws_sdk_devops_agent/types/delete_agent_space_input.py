"""Generated from Smithy shape ``com.amazonaws.devopsagent#DeleteAgentSpaceInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_devops_agent.types.agent_space_id


class DeleteAgentSpaceInput(TypedDict):
    agent_space_id: "aws_sdk_devops_agent.types.agent_space_id.AgentSpaceId"
    """<p>The unique identifier of the AgentSpace</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteAgentSpaceInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteAgentSpaceInput:
    out: DeleteAgentSpaceInput = {}  # type: ignore[typeddict-item]
    return out
