"""Generated from Smithy shape ``com.amazonaws.bedrockagent#GetAgentActionGroupResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent.types.agent_action_group


class GetAgentActionGroupResponse(TypedDict, closed=True):
    agent_action_group: "capo_bedrock_agent.types.agent_action_group.AgentActionGroup"
    """<p>Contains details about the action group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAgentActionGroupResponse) -> dict:
    out: dict = {}
    import capo_bedrock_agent.types.agent_action_group

    out["agentActionGroup"] = (
        capo_bedrock_agent.types.agent_action_group.serialize_json(
            value["agent_action_group"]
        )
    )
    return out


def deserialize_json(data: dict) -> GetAgentActionGroupResponse:
    out: GetAgentActionGroupResponse = {}  # type: ignore[typeddict-item]
    if "agentActionGroup" in data:
        import capo_bedrock_agent.types.agent_action_group

        out["agent_action_group"] = (
            capo_bedrock_agent.types.agent_action_group.deserialize_json(
                data["agentActionGroup"]
            )
        )
    else:
        raise DeserializationError(
            "GetAgentActionGroupResponse.agent_action_group required"
        )
    return out
