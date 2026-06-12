"""Generated from Smithy shape ``com.amazonaws.bedrockagent#AgentAliasRoutingConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.agent_alias_routing_configuration_list_item

AgentAliasRoutingConfiguration: TypeAlias = list[
    "aws_sdk_bedrock_agent.types.agent_alias_routing_configuration_list_item.AgentAliasRoutingConfigurationListItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: AgentAliasRoutingConfiguration) -> list:
    import aws_sdk_bedrock_agent.types.agent_alias_routing_configuration_list_item

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock_agent.types.agent_alias_routing_configuration_list_item.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AgentAliasRoutingConfiguration:
    import aws_sdk_bedrock_agent.types.agent_alias_routing_configuration_list_item

    out: AgentAliasRoutingConfiguration = []
    for item in data:
        out.append(
            aws_sdk_bedrock_agent.types.agent_alias_routing_configuration_list_item.deserialize_json(
                item
            )
        )
    return out
