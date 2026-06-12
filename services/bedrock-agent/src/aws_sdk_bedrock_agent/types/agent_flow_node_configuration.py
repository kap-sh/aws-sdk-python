"""Generated from Smithy shape ``com.amazonaws.bedrockagent#AgentFlowNodeConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.flow_agent_alias_arn


class AgentFlowNodeConfiguration(TypedDict):
    agent_alias_arn: (
        "aws_sdk_bedrock_agent.types.flow_agent_alias_arn.FlowAgentAliasArn"
    )
    """<p>The Amazon Resource Name (ARN) of the alias of the agent to invoke.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AgentFlowNodeConfiguration) -> dict:
    out: dict = {}
    out["agentAliasArn"] = value.get("agent_alias_arn", "")
    return out


def deserialize_json(data: dict) -> AgentFlowNodeConfiguration:
    out: AgentFlowNodeConfiguration = {}  # type: ignore[typeddict-item]
    if "agentAliasArn" in data:
        out["agent_alias_arn"] = data["agentAliasArn"]
    else:
        out["agent_alias_arn"] = ""
    return out
