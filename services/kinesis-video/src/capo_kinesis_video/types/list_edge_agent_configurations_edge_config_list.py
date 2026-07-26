"""Generated from Smithy shape ``com.amazonaws.kinesisvideo#ListEdgeAgentConfigurationsEdgeConfigList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kinesis_video.types.list_edge_agent_configurations_edge_config

ListEdgeAgentConfigurationsEdgeConfigList: TypeAlias = list[
    "capo_kinesis_video.types.list_edge_agent_configurations_edge_config.ListEdgeAgentConfigurationsEdgeConfig"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListEdgeAgentConfigurationsEdgeConfigList) -> list:
    import capo_kinesis_video.types.list_edge_agent_configurations_edge_config

    out: list = []
    for item in value:
        out.append(
            capo_kinesis_video.types.list_edge_agent_configurations_edge_config.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ListEdgeAgentConfigurationsEdgeConfigList:
    import capo_kinesis_video.types.list_edge_agent_configurations_edge_config

    out: ListEdgeAgentConfigurationsEdgeConfigList = []
    for item in data:
        out.append(
            capo_kinesis_video.types.list_edge_agent_configurations_edge_config.deserialize_json(
                item
            )
        )
    return out
