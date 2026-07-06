"""Generated from Smithy shape ``com.amazonaws.bedrockagent#GetAgentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.id


class GetAgentRequest(TypedDict, closed=True):
    agent_id: "aws_sdk_bedrock_agent.types.id.Id"
    """<p>The unique identifier of the agent.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAgentRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetAgentRequest:
    out: GetAgentRequest = {}  # type: ignore[typeddict-item]
    return out
