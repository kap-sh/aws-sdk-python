"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#NodeInputField``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock_agent_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.flow_node_input_category
    import aws_sdk_bedrock_agent_runtime.types.flow_node_io_data_type
    import aws_sdk_bedrock_agent_runtime.types.node_execution_content
    import aws_sdk_bedrock_agent_runtime.types.node_input_execution_chain
    import aws_sdk_bedrock_agent_runtime.types.node_input_name
    import aws_sdk_bedrock_agent_runtime.types.node_input_source


class NodeInputField(TypedDict, closed=True):
    name: "aws_sdk_bedrock_agent_runtime.types.node_input_name.NodeInputName"
    """<p>The name of the input field as defined in the node's input schema.</p>"""
    content: "aws_sdk_bedrock_agent_runtime.types.node_execution_content.NodeExecutionContent"
    """<p>The content of the input field, which can contain text or structured data.</p>"""
    source: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.node_input_source.NodeInputSource"
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
        "aws_sdk_bedrock_agent_runtime.types.node_input_execution_chain.NodeInputExecutionChain"
    ]
    """<p>The execution path through nested nodes like iterators and loops.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NodeInputField) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import aws_sdk_bedrock_agent_runtime.types.node_execution_content

    out["content"] = (
        aws_sdk_bedrock_agent_runtime.types.node_execution_content.serialize_json(
            value["content"]
        )
    )
    if "source" in value:
        import aws_sdk_bedrock_agent_runtime.types.node_input_source

        out["source"] = (
            aws_sdk_bedrock_agent_runtime.types.node_input_source.serialize_json(
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
        import aws_sdk_bedrock_agent_runtime.types.node_input_execution_chain

        out["executionChain"] = (
            aws_sdk_bedrock_agent_runtime.types.node_input_execution_chain.serialize_json(
                value["execution_chain"]
            )
        )
    return out


def deserialize_json(data: dict) -> NodeInputField:
    out: NodeInputField = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("NodeInputField.name required")
    if "content" in data:
        import aws_sdk_bedrock_agent_runtime.types.node_execution_content

        out["content"] = (
            aws_sdk_bedrock_agent_runtime.types.node_execution_content.deserialize_json(
                data["content"]
            )
        )
    else:
        raise DeserializationError("NodeInputField.content required")
    if "source" in data:
        import aws_sdk_bedrock_agent_runtime.types.node_input_source

        out["source"] = (
            aws_sdk_bedrock_agent_runtime.types.node_input_source.deserialize_json(
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
        import aws_sdk_bedrock_agent_runtime.types.node_input_execution_chain

        out["execution_chain"] = (
            aws_sdk_bedrock_agent_runtime.types.node_input_execution_chain.deserialize_json(
                data["executionChain"]
            )
        )
    return out
