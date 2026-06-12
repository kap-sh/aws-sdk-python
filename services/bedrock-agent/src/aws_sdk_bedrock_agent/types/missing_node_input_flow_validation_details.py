"""Generated from Smithy shape ``com.amazonaws.bedrockagent#MissingNodeInputFlowValidationDetails``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.flow_node_input_name
    import aws_sdk_bedrock_agent.types.flow_node_name


class MissingNodeInputFlowValidationDetails(TypedDict):
    node: "aws_sdk_bedrock_agent.types.flow_node_name.FlowNodeName"
    """<p>The name of the node missing the required input.</p>"""
    input: "aws_sdk_bedrock_agent.types.flow_node_input_name.FlowNodeInputName"
    """<p>The name of the missing input.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MissingNodeInputFlowValidationDetails) -> dict:
    out: dict = {}
    out["node"] = value["node"]
    out["input"] = value["input"]
    return out


def deserialize_json(data: dict) -> MissingNodeInputFlowValidationDetails:
    out: MissingNodeInputFlowValidationDetails = {}  # type: ignore[typeddict-item]
    if "node" in data:
        out["node"] = data["node"]
    else:
        raise DeserializationError(
            "MissingNodeInputFlowValidationDetails.node required"
        )
    if "input" in data:
        out["input"] = data["input"]
    else:
        raise DeserializationError(
            "MissingNodeInputFlowValidationDetails.input required"
        )
    return out
