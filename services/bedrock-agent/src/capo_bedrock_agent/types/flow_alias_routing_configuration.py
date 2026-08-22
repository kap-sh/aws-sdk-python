"""Generated from Smithy shape ``com.amazonaws.bedrockagent#FlowAliasRoutingConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agent.types.flow_alias_routing_configuration_list_item

FlowAliasRoutingConfiguration: TypeAlias = list[
    "capo_bedrock_agent.types.flow_alias_routing_configuration_list_item.FlowAliasRoutingConfigurationListItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: FlowAliasRoutingConfiguration) -> list:
    import capo_bedrock_agent.types.flow_alias_routing_configuration_list_item

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agent.types.flow_alias_routing_configuration_list_item.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> FlowAliasRoutingConfiguration:
    import capo_bedrock_agent.types.flow_alias_routing_configuration_list_item

    out: FlowAliasRoutingConfiguration = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agent.types.flow_alias_routing_configuration_list_item.deserialize_json(
                item
            )
        )
    return out
