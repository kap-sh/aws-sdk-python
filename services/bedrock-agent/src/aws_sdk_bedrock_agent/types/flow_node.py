"""Generated from Smithy shape ``com.amazonaws.bedrockagent#FlowNode``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.flow_node_configuration
    import aws_sdk_bedrock_agent.types.flow_node_inputs
    import aws_sdk_bedrock_agent.types.flow_node_name
    import aws_sdk_bedrock_agent.types.flow_node_outputs
    import aws_sdk_bedrock_agent.types.flow_node_type


class FlowNode(TypedDict, closed=True):
    name: "aws_sdk_bedrock_agent.types.flow_node_name.FlowNodeName"
    """<p>A name for the node.</p>"""
    type: "aws_sdk_bedrock_agent.types.flow_node_type.FlowNodeType"
    """<p>The type of node. This value must match the name of the key that you provide in the configuration you provide in the <code>FlowNodeConfiguration</code> field.</p>"""
    configuration: NotRequired[
        "aws_sdk_bedrock_agent.types.flow_node_configuration.FlowNodeConfiguration"
    ]
    """<p>Contains configurations for the node.</p>"""
    inputs: NotRequired["aws_sdk_bedrock_agent.types.flow_node_inputs.FlowNodeInputs"]
    """<p>An array of objects, each of which contains information about an input into the node.</p>"""
    outputs: NotRequired[
        "aws_sdk_bedrock_agent.types.flow_node_outputs.FlowNodeOutputs"
    ]
    """<p>A list of objects, each of which contains information about an output from the node.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FlowNode) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import aws_sdk_bedrock_agent.types.flow_node_type

    out["type"] = aws_sdk_bedrock_agent.types.flow_node_type.serialize_json(
        value["type"]
    )
    if "configuration" in value:
        import aws_sdk_bedrock_agent.types.flow_node_configuration

        out["configuration"] = (
            aws_sdk_bedrock_agent.types.flow_node_configuration.serialize_json(
                value["configuration"]
            )
        )
    if "inputs" in value:
        import aws_sdk_bedrock_agent.types.flow_node_inputs

        out["inputs"] = aws_sdk_bedrock_agent.types.flow_node_inputs.serialize_json(
            value["inputs"]
        )
    if "outputs" in value:
        import aws_sdk_bedrock_agent.types.flow_node_outputs

        out["outputs"] = aws_sdk_bedrock_agent.types.flow_node_outputs.serialize_json(
            value["outputs"]
        )
    return out


def deserialize_json(data: dict) -> FlowNode:
    out: FlowNode = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("FlowNode.name required")
    if "type" in data:
        import aws_sdk_bedrock_agent.types.flow_node_type

        out["type"] = aws_sdk_bedrock_agent.types.flow_node_type.deserialize_json(
            data["type"]
        )
    else:
        raise DeserializationError("FlowNode.type required")
    if "configuration" in data:
        import aws_sdk_bedrock_agent.types.flow_node_configuration

        out["configuration"] = (
            aws_sdk_bedrock_agent.types.flow_node_configuration.deserialize_json(
                data["configuration"]
            )
        )
    if "inputs" in data:
        import aws_sdk_bedrock_agent.types.flow_node_inputs

        out["inputs"] = aws_sdk_bedrock_agent.types.flow_node_inputs.deserialize_json(
            data["inputs"]
        )
    if "outputs" in data:
        import aws_sdk_bedrock_agent.types.flow_node_outputs

        out["outputs"] = aws_sdk_bedrock_agent.types.flow_node_outputs.deserialize_json(
            data["outputs"]
        )
    return out
