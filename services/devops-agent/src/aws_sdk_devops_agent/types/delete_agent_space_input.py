"""Generated from Smithy shape ``com.amazonaws.devopsagent#DeleteAgentSpaceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_devops_agent.types.agent_space_id


class DeleteAgentSpaceInput(TypedDict, closed=True):
    agent_space_id: "aws_sdk_devops_agent.types.agent_space_id.AgentSpaceId"
    """<p>The unique identifier of the AgentSpace</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteAgentSpaceInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteAgentSpaceInput:
    out: DeleteAgentSpaceInput = {}  # type: ignore[typeddict-item]
    return out
