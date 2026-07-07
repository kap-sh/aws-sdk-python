"""Generated from Smithy shape ``com.amazonaws.bedrockagent#AgentDescriptor``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.agent_alias_arn


class AgentDescriptor(TypedDict, closed=True):
    alias_arn: NotRequired["aws_sdk_bedrock_agent.types.agent_alias_arn.AgentAliasArn"]
    """<p>The agent's alias ARN.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AgentDescriptor) -> dict:
    out: dict = {}
    if "alias_arn" in value:
        out["aliasArn"] = value["alias_arn"]
    return out


def deserialize_json(data: dict) -> AgentDescriptor:
    out: AgentDescriptor = {}  # type: ignore[typeddict-item]
    if "aliasArn" in data:
        out["alias_arn"] = data["aliasArn"]
    return out
