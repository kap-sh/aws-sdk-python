"""Generated from Smithy shape ``com.amazonaws.bedrockagent#FlowConnection``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent.types.flow_connection_configuration
    import capo_bedrock_agent.types.flow_connection_name
    import capo_bedrock_agent.types.flow_connection_type
    import capo_bedrock_agent.types.flow_node_name


class FlowConnection(TypedDict, closed=True):
    type: "capo_bedrock_agent.types.flow_connection_type.FlowConnectionType"
    """<p>Whether the source node that the connection begins from is a condition node (<code>Conditional</code>) or not (<code>Data</code>).</p>"""
    name: "capo_bedrock_agent.types.flow_connection_name.FlowConnectionName"
    """<p>A name for the connection that you can reference.</p>"""
    source: "capo_bedrock_agent.types.flow_node_name.FlowNodeName"
    """<p>The node that the connection starts at.</p>"""
    target: "capo_bedrock_agent.types.flow_node_name.FlowNodeName"
    """<p>The node that the connection ends at.</p>"""
    configuration: NotRequired[
        "capo_bedrock_agent.types.flow_connection_configuration.FlowConnectionConfiguration"
    ]
    """<p>The configuration of the connection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FlowConnection) -> dict:
    out: dict = {}
    import capo_bedrock_agent.types.flow_connection_type

    out["type"] = capo_bedrock_agent.types.flow_connection_type.serialize_json(
        value["type"]
    )
    out["name"] = value["name"]
    out["source"] = value["source"]
    out["target"] = value["target"]
    if "configuration" in value:
        import capo_bedrock_agent.types.flow_connection_configuration

        out["configuration"] = (
            capo_bedrock_agent.types.flow_connection_configuration.serialize_json(
                value["configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> FlowConnection:
    out: FlowConnection = {}  # type: ignore[typeddict-item]
    if "type" in data:
        import capo_bedrock_agent.types.flow_connection_type

        out["type"] = capo_bedrock_agent.types.flow_connection_type.deserialize_json(
            data["type"]
        )
    else:
        raise DeserializationError("FlowConnection.type required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("FlowConnection.name required")
    if "source" in data:
        out["source"] = data["source"]
    else:
        raise DeserializationError("FlowConnection.source required")
    if "target" in data:
        out["target"] = data["target"]
    else:
        raise DeserializationError("FlowConnection.target required")
    if "configuration" in data:
        import capo_bedrock_agent.types.flow_connection_configuration

        out["configuration"] = (
            capo_bedrock_agent.types.flow_connection_configuration.deserialize_json(
                data["configuration"]
            )
        )
    return out
