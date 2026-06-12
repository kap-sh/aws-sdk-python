"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#A2aDescriptor``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.agent_card_definition

class A2aDescriptor(TypedDict):
    agent_card: NotRequired["aws_sdk_bedrock_agentcore_control.types.agent_card_definition.AgentCardDefinition"]
    """<p>The agent card definition for the A2A agent, as defined by the A2A protocol specification.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: A2aDescriptor) -> dict:
    out: dict = {}
    if "agent_card" in value:
        import aws_sdk_bedrock_agentcore_control.types.agent_card_definition
        out["agentCard"] = aws_sdk_bedrock_agentcore_control.types.agent_card_definition.serialize_json(value["agent_card"])
    return out


def deserialize_json(data: dict) -> A2aDescriptor:
    out: A2aDescriptor = {}  # type: ignore[typeddict-item]
    if "agentCard" in data:
        import aws_sdk_bedrock_agentcore_control.types.agent_card_definition
        out["agent_card"] = aws_sdk_bedrock_agentcore_control.types.agent_card_definition.deserialize_json(data["agentCard"])
    return out