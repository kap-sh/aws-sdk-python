"""Generated from Smithy shape ``com.amazonaws.bedrockagent#FlowDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.flow_connections
    import aws_sdk_bedrock_agent.types.flow_nodes


class FlowDefinition(TypedDict, closed=True):
    nodes: NotRequired["aws_sdk_bedrock_agent.types.flow_nodes.FlowNodes"]
    """<p>An array of node definitions in the flow.</p>"""
    connections: NotRequired[
        "aws_sdk_bedrock_agent.types.flow_connections.FlowConnections"
    ]
    """<p>An array of connection definitions in the flow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FlowDefinition) -> dict:
    out: dict = {}
    if "nodes" in value:
        import aws_sdk_bedrock_agent.types.flow_nodes

        out["nodes"] = aws_sdk_bedrock_agent.types.flow_nodes.serialize_json(
            value["nodes"]
        )
    if "connections" in value:
        import aws_sdk_bedrock_agent.types.flow_connections

        out["connections"] = (
            aws_sdk_bedrock_agent.types.flow_connections.serialize_json(
                value["connections"]
            )
        )
    return out


def deserialize_json(data: dict) -> FlowDefinition:
    out: FlowDefinition = {}  # type: ignore[typeddict-item]
    if "nodes" in data:
        import aws_sdk_bedrock_agent.types.flow_nodes

        out["nodes"] = aws_sdk_bedrock_agent.types.flow_nodes.deserialize_json(
            data["nodes"]
        )
    if "connections" in data:
        import aws_sdk_bedrock_agent.types.flow_connections

        out["connections"] = (
            aws_sdk_bedrock_agent.types.flow_connections.deserialize_json(
                data["connections"]
            )
        )
    return out
