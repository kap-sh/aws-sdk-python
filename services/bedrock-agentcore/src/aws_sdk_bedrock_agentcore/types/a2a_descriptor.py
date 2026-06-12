"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#A2aDescriptor``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_bedrock_agentcore.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.agent_card_definition

class A2aDescriptor(TypedDict):
    agent_card: "aws_sdk_bedrock_agentcore.types.agent_card_definition.AgentCardDefinition"
    """<p> The agent card definition that describes the agent's capabilities and interface.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: A2aDescriptor) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agentcore.types.agent_card_definition
    out["agentCard"] = aws_sdk_bedrock_agentcore.types.agent_card_definition.serialize_json(value["agent_card"])
    return out


def deserialize_json(data: dict) -> A2aDescriptor:
    out: A2aDescriptor = {}  # type: ignore[typeddict-item]
    if "agentCard" in data:
        import aws_sdk_bedrock_agentcore.types.agent_card_definition
        out["agent_card"] = aws_sdk_bedrock_agentcore.types.agent_card_definition.deserialize_json(data["agentCard"])
    else:
        raise DeserializationError("A2aDescriptor.agent_card required")
    return out