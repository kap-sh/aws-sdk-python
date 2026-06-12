"""Generated from Smithy shape ``com.amazonaws.bedrockagent#AgentAliasRoutingConfigurationListItem``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.provisioned_model_identifier
    import aws_sdk_bedrock_agent.types.version


class AgentAliasRoutingConfigurationListItem(TypedDict):
    agent_version: NotRequired["aws_sdk_bedrock_agent.types.version.Version"]
    """<p>The version of the agent with which the alias is associated.</p>"""
    provisioned_throughput: NotRequired[
        "aws_sdk_bedrock_agent.types.provisioned_model_identifier.ProvisionedModelIdentifier"
    ]
    """<p>Information on the Provisioned Throughput assigned to an agent alias.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AgentAliasRoutingConfigurationListItem) -> dict:
    out: dict = {}
    if "agent_version" in value:
        out["agentVersion"] = value["agent_version"]
    if "provisioned_throughput" in value:
        out["provisionedThroughput"] = value["provisioned_throughput"]
    return out


def deserialize_json(data: dict) -> AgentAliasRoutingConfigurationListItem:
    out: AgentAliasRoutingConfigurationListItem = {}  # type: ignore[typeddict-item]
    if "agentVersion" in data:
        out["agent_version"] = data["agentVersion"]
    if "provisionedThroughput" in data:
        out["provisioned_throughput"] = data["provisionedThroughput"]
    return out
