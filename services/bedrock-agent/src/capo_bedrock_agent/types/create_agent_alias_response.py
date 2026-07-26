"""Generated from Smithy shape ``com.amazonaws.bedrockagent#CreateAgentAliasResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent.types.agent_alias


class CreateAgentAliasResponse(TypedDict, closed=True):
    agent_alias: "capo_bedrock_agent.types.agent_alias.AgentAlias"
    """<p>Contains details about the alias that was created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAgentAliasResponse) -> dict:
    out: dict = {}
    import capo_bedrock_agent.types.agent_alias

    out["agentAlias"] = capo_bedrock_agent.types.agent_alias.serialize_json(
        value["agent_alias"]
    )
    return out


def deserialize_json(data: dict) -> CreateAgentAliasResponse:
    out: CreateAgentAliasResponse = {}  # type: ignore[typeddict-item]
    if "agentAlias" in data:
        import capo_bedrock_agent.types.agent_alias

        out["agent_alias"] = capo_bedrock_agent.types.agent_alias.deserialize_json(
            data["agentAlias"]
        )
    else:
        raise DeserializationError("CreateAgentAliasResponse.agent_alias required")
    return out
