"""Generated from Smithy shape ``com.amazonaws.bedrockagent#FlowNodeOutput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.flow_node_io_data_type
    import aws_sdk_bedrock_agent.types.flow_node_output_name


class FlowNodeOutput(TypedDict):
    name: "aws_sdk_bedrock_agent.types.flow_node_output_name.FlowNodeOutputName"
    """<p>A name for the output that you can reference.</p>"""
    type: "aws_sdk_bedrock_agent.types.flow_node_io_data_type.FlowNodeIODataType"
    """<p>The data type of the output. If the output doesn't match this type at runtime, a validation error will be thrown.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FlowNodeOutput) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import aws_sdk_bedrock_agent.types.flow_node_io_data_type

    out["type"] = aws_sdk_bedrock_agent.types.flow_node_io_data_type.serialize_json(
        value["type"]
    )
    return out


def deserialize_json(data: dict) -> FlowNodeOutput:
    out: FlowNodeOutput = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("FlowNodeOutput.name required")
    if "type" in data:
        import aws_sdk_bedrock_agent.types.flow_node_io_data_type

        out["type"] = (
            aws_sdk_bedrock_agent.types.flow_node_io_data_type.deserialize_json(
                data["type"]
            )
        )
    else:
        raise DeserializationError("FlowNodeOutput.type required")
    return out
