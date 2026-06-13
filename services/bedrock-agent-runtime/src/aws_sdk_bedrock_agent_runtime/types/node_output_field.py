"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#NodeOutputField``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_agent_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.flow_node_io_data_type
    import aws_sdk_bedrock_agent_runtime.types.node_execution_content
    import aws_sdk_bedrock_agent_runtime.types.node_output_name
    import aws_sdk_bedrock_agent_runtime.types.node_output_next_list


class NodeOutputField(TypedDict):
    name: "aws_sdk_bedrock_agent_runtime.types.node_output_name.NodeOutputName"
    """<p>The name of the output field as defined in the node's output schema.</p>"""
    content: "aws_sdk_bedrock_agent_runtime.types.node_execution_content.NodeExecutionContent"
    """<p>The content of the output field, which can contain text or structured data.</p>"""
    next: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.node_output_next_list.NodeOutputNextList"
    ]
    """<p>The next node that receives output data from this field.</p>"""
    type: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.flow_node_io_data_type.FlowNodeIODataType"
    ]
    """<p>The data type of the output field for compatibility validation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NodeOutputField) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import aws_sdk_bedrock_agent_runtime.types.node_execution_content

    out["content"] = (
        aws_sdk_bedrock_agent_runtime.types.node_execution_content.serialize_json(
            value["content"]
        )
    )
    if "next" in value:
        import aws_sdk_bedrock_agent_runtime.types.node_output_next_list

        out["next"] = (
            aws_sdk_bedrock_agent_runtime.types.node_output_next_list.serialize_json(
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


def deserialize_json(data: dict) -> NodeOutputField:
    out: NodeOutputField = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("NodeOutputField.name required")
    if "content" in data:
        import aws_sdk_bedrock_agent_runtime.types.node_execution_content

        out["content"] = (
            aws_sdk_bedrock_agent_runtime.types.node_execution_content.deserialize_json(
                data["content"]
            )
        )
    else:
        raise DeserializationError("NodeOutputField.content required")
    if "next" in data:
        import aws_sdk_bedrock_agent_runtime.types.node_output_next_list

        out["next"] = (
            aws_sdk_bedrock_agent_runtime.types.node_output_next_list.deserialize_json(
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
