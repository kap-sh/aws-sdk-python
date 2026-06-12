"""Generated from Smithy shape ``com.amazonaws.bedrockagent#GetAgentAliasResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.agent_alias


class GetAgentAliasResponse(TypedDict):
    agent_alias: "aws_sdk_bedrock_agent.types.agent_alias.AgentAlias"
    """<p>Contains information about the alias.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAgentAliasResponse) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agent.types.agent_alias

    out["agentAlias"] = aws_sdk_bedrock_agent.types.agent_alias.serialize_json(
        value["agent_alias"]
    )
    return out


def deserialize_json(data: dict) -> GetAgentAliasResponse:
    out: GetAgentAliasResponse = {}  # type: ignore[typeddict-item]
    if "agentAlias" in data:
        import aws_sdk_bedrock_agent.types.agent_alias

        out["agent_alias"] = aws_sdk_bedrock_agent.types.agent_alias.deserialize_json(
            data["agentAlias"]
        )
    else:
        raise DeserializationError("GetAgentAliasResponse.agent_alias required")
    return out
