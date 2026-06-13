"""Generated from Smithy shape ``com.amazonaws.devopsagent#GetOperatorAppInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_devops_agent.types.agent_space_id


class GetOperatorAppInput(TypedDict):
    agent_space_id: "aws_sdk_devops_agent.types.agent_space_id.AgentSpaceId"
    """<p>The unique identifier of the AgentSpace</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetOperatorAppInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetOperatorAppInput:
    out: GetOperatorAppInput = {}  # type: ignore[typeddict-item]
    return out
