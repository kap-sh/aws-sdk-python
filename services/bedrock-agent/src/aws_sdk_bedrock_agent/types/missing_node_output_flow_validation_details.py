"""Generated from Smithy shape ``com.amazonaws.bedrockagent#MissingNodeOutputFlowValidationDetails``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.flow_node_name
    import aws_sdk_bedrock_agent.types.flow_node_output_name


class MissingNodeOutputFlowValidationDetails(TypedDict):
    node: "aws_sdk_bedrock_agent.types.flow_node_name.FlowNodeName"
    """<p>The name of the node missing the required output.</p>"""
    output: "aws_sdk_bedrock_agent.types.flow_node_output_name.FlowNodeOutputName"
    """<p>The name of the missing output.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MissingNodeOutputFlowValidationDetails) -> dict:
    out: dict = {}
    out["node"] = value["node"]
    out["output"] = value["output"]
    return out


def deserialize_json(data: dict) -> MissingNodeOutputFlowValidationDetails:
    out: MissingNodeOutputFlowValidationDetails = {}  # type: ignore[typeddict-item]
    if "node" in data:
        out["node"] = data["node"]
    else:
        raise DeserializationError(
            "MissingNodeOutputFlowValidationDetails.node required"
        )
    if "output" in data:
        out["output"] = data["output"]
    else:
        raise DeserializationError(
            "MissingNodeOutputFlowValidationDetails.output required"
        )
    return out
