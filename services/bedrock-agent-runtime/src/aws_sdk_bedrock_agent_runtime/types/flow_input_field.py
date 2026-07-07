"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#FlowInputField``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_bedrock_agent_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.flow_execution_content
    import aws_sdk_bedrock_agent_runtime.types.node_input_name


class FlowInputField(TypedDict, closed=True):
    name: "aws_sdk_bedrock_agent_runtime.types.node_input_name.NodeInputName"
    """<p>The name of the input field as defined in the flow's input schema.</p>"""
    content: "aws_sdk_bedrock_agent_runtime.types.flow_execution_content.FlowExecutionContent"
    """<p>The content of the input field, which can contain text or structured data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FlowInputField) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import aws_sdk_bedrock_agent_runtime.types.flow_execution_content

    out["content"] = (
        aws_sdk_bedrock_agent_runtime.types.flow_execution_content.serialize_json(
            value["content"]
        )
    )
    return out


def deserialize_json(data: dict) -> FlowInputField:
    out: FlowInputField = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("FlowInputField.name required")
    if "content" in data:
        import aws_sdk_bedrock_agent_runtime.types.flow_execution_content

        out["content"] = (
            aws_sdk_bedrock_agent_runtime.types.flow_execution_content.deserialize_json(
                data["content"]
            )
        )
    else:
        raise DeserializationError("FlowInputField.content required")
    return out
