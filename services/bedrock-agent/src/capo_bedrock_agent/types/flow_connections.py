"""Generated from Smithy shape ``com.amazonaws.bedrockagent#FlowConnections``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agent.types.flow_connection

FlowConnections: TypeAlias = list[
    "capo_bedrock_agent.types.flow_connection.FlowConnection"
]


# --- restJson1 ser/de ---
def serialize_json(value: FlowConnections) -> list:
    import capo_bedrock_agent.types.flow_connection

    out: list = []
    for item in value:
        out.append(capo_bedrock_agent.types.flow_connection.serialize_json(item))
    return out


def deserialize_json(data: list) -> FlowConnections:
    import capo_bedrock_agent.types.flow_connection

    out: FlowConnections = []
    for item in data:
        out.append(capo_bedrock_agent.types.flow_connection.deserialize_json(item))
    return out
