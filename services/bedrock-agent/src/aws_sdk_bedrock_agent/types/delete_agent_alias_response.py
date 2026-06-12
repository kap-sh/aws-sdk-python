"""Generated from Smithy shape ``com.amazonaws.bedrockagent#DeleteAgentAliasResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.agent_alias_id
    import aws_sdk_bedrock_agent.types.agent_alias_status
    import aws_sdk_bedrock_agent.types.id


class DeleteAgentAliasResponse(TypedDict):
    agent_id: "aws_sdk_bedrock_agent.types.id.Id"
    """<p>The unique identifier of the agent that the alias belongs to.</p>"""
    agent_alias_id: "aws_sdk_bedrock_agent.types.agent_alias_id.AgentAliasId"
    """<p>The unique identifier of the alias that was deleted.</p>"""
    agent_alias_status: (
        "aws_sdk_bedrock_agent.types.agent_alias_status.AgentAliasStatus"
    )
    """<p>The status of the alias.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteAgentAliasResponse) -> dict:
    out: dict = {}
    out["agentId"] = value["agent_id"]
    out["agentAliasId"] = value["agent_alias_id"]
    import aws_sdk_bedrock_agent.types.agent_alias_status

    out["agentAliasStatus"] = (
        aws_sdk_bedrock_agent.types.agent_alias_status.serialize_json(
            value["agent_alias_status"]
        )
    )
    return out


def deserialize_json(data: dict) -> DeleteAgentAliasResponse:
    out: DeleteAgentAliasResponse = {}  # type: ignore[typeddict-item]
    if "agentId" in data:
        out["agent_id"] = data["agentId"]
    else:
        raise DeserializationError("DeleteAgentAliasResponse.agent_id required")
    if "agentAliasId" in data:
        out["agent_alias_id"] = data["agentAliasId"]
    else:
        raise DeserializationError("DeleteAgentAliasResponse.agent_alias_id required")
    if "agentAliasStatus" in data:
        import aws_sdk_bedrock_agent.types.agent_alias_status

        out["agent_alias_status"] = (
            aws_sdk_bedrock_agent.types.agent_alias_status.deserialize_json(
                data["agentAliasStatus"]
            )
        )
    else:
        raise DeserializationError(
            "DeleteAgentAliasResponse.agent_alias_status required"
        )
    return out
