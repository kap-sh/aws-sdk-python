"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#A2aDescriptor``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.agent_card_definition


class A2aDescriptor(TypedDict, closed=True):
    agent_card: NotRequired[
        "capo_bedrock_agentcore_control.types.agent_card_definition.AgentCardDefinition"
    ]
    """<p>The agent card definition for the A2A agent, as defined by the A2A protocol specification.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: A2aDescriptor) -> dict:
    out: dict = {}
    if "agent_card" in value:
        import capo_bedrock_agentcore_control.types.agent_card_definition

        out["agentCard"] = (
            capo_bedrock_agentcore_control.types.agent_card_definition.serialize_json(
                value["agent_card"]
            )
        )
    return out


def deserialize_json(data: dict) -> A2aDescriptor:
    out: A2aDescriptor = {}  # type: ignore[typeddict-item]
    if data.get("agentCard") is not None:
        import capo_bedrock_agentcore_control.types.agent_card_definition

        out["agent_card"] = (
            capo_bedrock_agentcore_control.types.agent_card_definition.deserialize_json(
                data["agentCard"]
            )
        )
    return out
