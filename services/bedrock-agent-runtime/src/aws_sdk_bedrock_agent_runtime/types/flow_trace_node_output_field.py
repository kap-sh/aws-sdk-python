"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#FlowTraceNodeOutputField``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_agent_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.flow_node_io_data_type
    import aws_sdk_bedrock_agent_runtime.types.flow_trace_node_output_content
    import aws_sdk_bedrock_agent_runtime.types.flow_trace_node_output_next_list
    import aws_sdk_bedrock_agent_runtime.types.node_output_name


class FlowTraceNodeOutputField(TypedDict):
    node_output_name: (
        "aws_sdk_bedrock_agent_runtime.types.node_output_name.NodeOutputName"
    )
    """<p>The name of the node output.</p>"""
    content: "aws_sdk_bedrock_agent_runtime.types.flow_trace_node_output_content.FlowTraceNodeOutputContent"
    """<p>The content of the node output.</p>"""
    next: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.flow_trace_node_output_next_list.FlowTraceNodeOutputNextList"
    ]
    """<p>The next node that receives output data from this field.</p>"""
    type: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.flow_node_io_data_type.FlowNodeIODataType"
    ]
    """<p>The data type of the output field for compatibility validation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FlowTraceNodeOutputField) -> dict:
    out: dict = {}
    out["nodeOutputName"] = value["node_output_name"]
    import aws_sdk_bedrock_agent_runtime.types.flow_trace_node_output_content

    out["content"] = (
        aws_sdk_bedrock_agent_runtime.types.flow_trace_node_output_content.serialize_json(
            value["content"]
        )
    )
    if "next" in value:
        import aws_sdk_bedrock_agent_runtime.types.flow_trace_node_output_next_list

        out["next"] = (
            aws_sdk_bedrock_agent_runtime.types.flow_trace_node_output_next_list.serialize_json(
                value["next"]
            )
        )
    if "type" in value:
        import aws_sdk_bedrock_agent_runtime.types.flow_node_io_data_type

        out["type"] = (
            aws_sdk_bedrock_agent_runtime.types.flow_node_io_data_type.serialize_json(
                value["type"]
            )
        )
    return out


def deserialize_json(data: dict) -> FlowTraceNodeOutputField:
    out: FlowTraceNodeOutputField = {}  # type: ignore[typeddict-item]
    if "nodeOutputName" in data:
        out["node_output_name"] = data["nodeOutputName"]
    else:
        raise DeserializationError("FlowTraceNodeOutputField.node_output_name required")
    if "content" in data:
        import aws_sdk_bedrock_agent_runtime.types.flow_trace_node_output_content

        out["content"] = (
            aws_sdk_bedrock_agent_runtime.types.flow_trace_node_output_content.deserialize_json(
                data["content"]
            )
        )
    else:
        raise DeserializationError("FlowTraceNodeOutputField.content required")
    if "next" in data:
        import aws_sdk_bedrock_agent_runtime.types.flow_trace_node_output_next_list

        out["next"] = (
            aws_sdk_bedrock_agent_runtime.types.flow_trace_node_output_next_list.deserialize_json(
                data["next"]
            )
        )
    if "type" in data:
        import aws_sdk_bedrock_agent_runtime.types.flow_node_io_data_type

        out["type"] = (
            aws_sdk_bedrock_agent_runtime.types.flow_node_io_data_type.deserialize_json(
                data["type"]
            )
        )
    return out
