"""Generated from Smithy shape ``com.amazonaws.bedrockagent#FlowDataConnectionConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.flow_node_input_name
    import aws_sdk_bedrock_agent.types.flow_node_output_name


class FlowDataConnectionConfiguration(TypedDict, closed=True):
    source_output: (
        "aws_sdk_bedrock_agent.types.flow_node_output_name.FlowNodeOutputName"
    )
    """<p>The name of the output in the source node that the connection begins from.</p>"""
    target_input: "aws_sdk_bedrock_agent.types.flow_node_input_name.FlowNodeInputName"
    """<p>The name of the input in the target node that the connection ends at.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FlowDataConnectionConfiguration) -> dict:
    out: dict = {}
    out["sourceOutput"] = value["source_output"]
    out["targetInput"] = value["target_input"]
    return out


def deserialize_json(data: dict) -> FlowDataConnectionConfiguration:
    out: FlowDataConnectionConfiguration = {}  # type: ignore[typeddict-item]
    if "sourceOutput" in data:
        out["source_output"] = data["sourceOutput"]
    else:
        raise DeserializationError(
            "FlowDataConnectionConfiguration.source_output required"
        )
    if "targetInput" in data:
        out["target_input"] = data["targetInput"]
    else:
        raise DeserializationError(
            "FlowDataConnectionConfiguration.target_input required"
        )
    return out
