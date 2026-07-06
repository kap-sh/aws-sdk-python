"""Generated from Smithy shape ``com.amazonaws.bedrockagent#MultipleNodeInputConnectionsFlowValidationDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.flow_node_input_name
    import aws_sdk_bedrock_agent.types.flow_node_name


class MultipleNodeInputConnectionsFlowValidationDetails(TypedDict, closed=True):
    node: "aws_sdk_bedrock_agent.types.flow_node_name.FlowNodeName"
    """<p>The name of the node containing the input with multiple connections.</p>"""
    input: "aws_sdk_bedrock_agent.types.flow_node_input_name.FlowNodeInputName"
    """<p>The name of the input with multiple connections to it.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MultipleNodeInputConnectionsFlowValidationDetails) -> dict:
    out: dict = {}
    out["node"] = value["node"]
    out["input"] = value["input"]
    return out


def deserialize_json(data: dict) -> MultipleNodeInputConnectionsFlowValidationDetails:
    out: MultipleNodeInputConnectionsFlowValidationDetails = {}  # type: ignore[typeddict-item]
    if "node" in data:
        out["node"] = data["node"]
    else:
        raise DeserializationError(
            "MultipleNodeInputConnectionsFlowValidationDetails.node required"
        )
    if "input" in data:
        out["input"] = data["input"]
    else:
        raise DeserializationError(
            "MultipleNodeInputConnectionsFlowValidationDetails.input required"
        )
    return out
