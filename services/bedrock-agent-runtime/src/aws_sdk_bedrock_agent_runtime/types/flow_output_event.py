"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#FlowOutputEvent``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock_agent_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.flow_output_content
    import aws_sdk_bedrock_agent_runtime.types.node_name
    import aws_sdk_bedrock_agent_runtime.types.node_type


class FlowOutputEvent(TypedDict):
    node_name: "aws_sdk_bedrock_agent_runtime.types.node_name.NodeName"
    """<p>The name of the flow output node that the output is from.</p>"""
    node_type: "aws_sdk_bedrock_agent_runtime.types.node_type.NodeType"
    """<p>The type of the node that the output is from.</p>"""
    content: "aws_sdk_bedrock_agent_runtime.types.flow_output_content.FlowOutputContent"
    """<p>The content in the output.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FlowOutputEvent) -> dict:
    out: dict = {}
    out["nodeName"] = value["node_name"]
    import aws_sdk_bedrock_agent_runtime.types.node_type

    out["nodeType"] = aws_sdk_bedrock_agent_runtime.types.node_type.serialize_json(
        value["node_type"]
    )
    import aws_sdk_bedrock_agent_runtime.types.flow_output_content

    out["content"] = (
        aws_sdk_bedrock_agent_runtime.types.flow_output_content.serialize_json(
            value["content"]
        )
    )
    return out


def deserialize_json(data: dict) -> FlowOutputEvent:
    out: FlowOutputEvent = {}  # type: ignore[typeddict-item]
    if "nodeName" in data:
        out["node_name"] = data["nodeName"]
    else:
        raise DeserializationError("FlowOutputEvent.node_name required")
    if "nodeType" in data:
        import aws_sdk_bedrock_agent_runtime.types.node_type

        out["node_type"] = (
            aws_sdk_bedrock_agent_runtime.types.node_type.deserialize_json(
                data["nodeType"]
            )
        )
    else:
        raise DeserializationError("FlowOutputEvent.node_type required")
    if "content" in data:
        import aws_sdk_bedrock_agent_runtime.types.flow_output_content

        out["content"] = (
            aws_sdk_bedrock_agent_runtime.types.flow_output_content.deserialize_json(
                data["content"]
            )
        )
    else:
        raise DeserializationError("FlowOutputEvent.content required")
    return out
