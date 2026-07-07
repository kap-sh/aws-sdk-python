"""Generated from Smithy shape ``com.amazonaws.bedrockagent#PrepareAgentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.id


class PrepareAgentRequest(TypedDict, closed=True):
    agent_id: "aws_sdk_bedrock_agent.types.id.Id"
    """<p>The unique identifier of the agent for which to create a <code>DRAFT</code> version.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PrepareAgentRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> PrepareAgentRequest:
    out: PrepareAgentRequest = {}  # type: ignore[typeddict-item]
    return out
