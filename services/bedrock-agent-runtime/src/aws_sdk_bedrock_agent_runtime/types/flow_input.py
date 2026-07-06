"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#FlowInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock_agent_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.flow_input_content
    import aws_sdk_bedrock_agent_runtime.types.node_input_name
    import aws_sdk_bedrock_agent_runtime.types.node_name
    import aws_sdk_bedrock_agent_runtime.types.node_output_name


class FlowInput(TypedDict, closed=True):
    node_name: "aws_sdk_bedrock_agent_runtime.types.node_name.NodeName"
    """<p>The name of the flow input node that begins the prompt flow.</p>"""
    node_output_name: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.node_output_name.NodeOutputName"
    ]
    """<p>The name of the output from the flow input node that begins the prompt flow.</p>"""
    content: "aws_sdk_bedrock_agent_runtime.types.flow_input_content.FlowInputContent"
    """<p>Contains information about an input into the prompt flow.</p>"""
    node_input_name: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.node_input_name.NodeInputName"
    ]
    """<p>The name of the input from the flow input node.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FlowInput) -> dict:
    out: dict = {}
    out["nodeName"] = value["node_name"]
    if "node_output_name" in value:
        out["nodeOutputName"] = value["node_output_name"]
    import aws_sdk_bedrock_agent_runtime.types.flow_input_content

    out["content"] = (
        aws_sdk_bedrock_agent_runtime.types.flow_input_content.serialize_json(
            value["content"]
        )
    )
    if "node_input_name" in value:
        out["nodeInputName"] = value["node_input_name"]
    return out


def deserialize_json(data: dict) -> FlowInput:
    out: FlowInput = {}  # type: ignore[typeddict-item]
    if "nodeName" in data:
        out["node_name"] = data["nodeName"]
    else:
        raise DeserializationError("FlowInput.node_name required")
    if "nodeOutputName" in data:
        out["node_output_name"] = data["nodeOutputName"]
    if "content" in data:
        import aws_sdk_bedrock_agent_runtime.types.flow_input_content

        out["content"] = (
            aws_sdk_bedrock_agent_runtime.types.flow_input_content.deserialize_json(
                data["content"]
            )
        )
    else:
        raise DeserializationError("FlowInput.content required")
    if "nodeInputName" in data:
        out["node_input_name"] = data["nodeInputName"]
    return out
