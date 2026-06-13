"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#FlowTraceNodeInputField``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_agent_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.flow_node_input_category
    import aws_sdk_bedrock_agent_runtime.types.flow_node_io_data_type
    import aws_sdk_bedrock_agent_runtime.types.flow_trace_node_input_content
    import aws_sdk_bedrock_agent_runtime.types.flow_trace_node_input_execution_chain
    import aws_sdk_bedrock_agent_runtime.types.flow_trace_node_input_source
    import aws_sdk_bedrock_agent_runtime.types.node_input_name


class FlowTraceNodeInputField(TypedDict):
    node_input_name: "aws_sdk_bedrock_agent_runtime.types.node_input_name.NodeInputName"
    """<p>The name of the node input.</p>"""
    content: "aws_sdk_bedrock_agent_runtime.types.flow_trace_node_input_content.FlowTraceNodeInputContent"
    """<p>The content of the node input.</p>"""
    source: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.flow_trace_node_input_source.FlowTraceNodeInputSource"
    ]
    """<p>The source node that provides input data to this field.</p>"""
    type: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.flow_node_io_data_type.FlowNodeIODataType"
    ]
    """<p>The data type of the input field for compatibility validation.</p>"""
    category: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.flow_node_input_category.FlowNodeInputCategory"
    ]
    """<p>The category of the input field.</p>"""
    execution_chain: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.flow_trace_node_input_execution_chain.FlowTraceNodeInputExecutionChain"
    ]
    """<p>The execution path through nested nodes like iterators and loops.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FlowTraceNodeInputField) -> dict:
    out: dict = {}
    out["nodeInputName"] = value["node_input_name"]
    import aws_sdk_bedrock_agent_runtime.types.flow_trace_node_input_content

    out["content"] = (
        aws_sdk_bedrock_agent_runtime.types.flow_trace_node_input_content.serialize_json(
            value["content"]
        )
    )
    if "source" in value:
        import aws_sdk_bedrock_agent_runtime.types.flow_trace_node_input_source

        out["source"] = (
            aws_sdk_bedrock_agent_runtime.types.flow_trace_node_input_source.serialize_json(
                value["source"]
            )
        )
    if "type" in value:
        import aws_sdk_bedrock_agent_runtime.types.flow_node_io_data_type

        out["type"] = (
            aws_sdk_bedrock_agent_runtime.types.flow_node_io_data_type.serialize_json(
                value["type"]
            )
        )
    if "category" in value:
        import aws_sdk_bedrock_agent_runtime.types.flow_node_input_category

        out["category"] = (
            aws_sdk_bedrock_agent_runtime.types.flow_node_input_category.serialize_json(
                value["category"]
            )
        )
    if "execution_chain" in value:
        import aws_sdk_bedrock_agent_runtime.types.flow_trace_node_input_execution_chain

        out["executionChain"] = (
            aws_sdk_bedrock_agent_runtime.types.flow_trace_node_input_execution_chain.serialize_json(
                value["execution_chain"]
            )
        )
    return out


def deserialize_json(data: dict) -> FlowTraceNodeInputField:
    out: FlowTraceNodeInputField = {}  # type: ignore[typeddict-item]
    if "nodeInputName" in data:
        out["node_input_name"] = data["nodeInputName"]
    else:
        raise DeserializationError("FlowTraceNodeInputField.node_input_name required")
    if "content" in data:
        import aws_sdk_bedrock_agent_runtime.types.flow_trace_node_input_content

        out["content"] = (
            aws_sdk_bedrock_agent_runtime.types.flow_trace_node_input_content.deserialize_json(
                data["content"]
            )
        )
    else:
        raise DeserializationError("FlowTraceNodeInputField.content required")
    if "source" in data:
        import aws_sdk_bedrock_agent_runtime.types.flow_trace_node_input_source

        out["source"] = (
            aws_sdk_bedrock_agent_runtime.types.flow_trace_node_input_source.deserialize_json(
                data["source"]
            )
        )
    if "type" in data:
        import aws_sdk_bedrock_agent_runtime.types.flow_node_io_data_type

        out["type"] = (
            aws_sdk_bedrock_agent_runtime.types.flow_node_io_data_type.deserialize_json(
                data["type"]
            )
        )
    if "category" in data:
        import aws_sdk_bedrock_agent_runtime.types.flow_node_input_category

        out["category"] = (
            aws_sdk_bedrock_agent_runtime.types.flow_node_input_category.deserialize_json(
                data["category"]
            )
        )
    if "executionChain" in data:
        import aws_sdk_bedrock_agent_runtime.types.flow_trace_node_input_execution_chain

        out["execution_chain"] = (
            aws_sdk_bedrock_agent_runtime.types.flow_trace_node_input_execution_chain.deserialize_json(
                data["executionChain"]
            )
        )
    return out
