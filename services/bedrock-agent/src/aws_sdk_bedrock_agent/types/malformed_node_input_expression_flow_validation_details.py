"""Generated from Smithy shape ``com.amazonaws.bedrockagent#MalformedNodeInputExpressionFlowValidationDetails``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.error_message
    import aws_sdk_bedrock_agent.types.flow_node_input_name
    import aws_sdk_bedrock_agent.types.flow_node_name


class MalformedNodeInputExpressionFlowValidationDetails(TypedDict):
    node: "aws_sdk_bedrock_agent.types.flow_node_name.FlowNodeName"
    """<p>The name of the node containing the malformed input expression.</p>"""
    input: "aws_sdk_bedrock_agent.types.flow_node_input_name.FlowNodeInputName"
    """<p>The name of the input with the malformed expression.</p>"""
    cause: "aws_sdk_bedrock_agent.types.error_message.ErrorMessage"
    """<p>The error message describing why the input expression is malformed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MalformedNodeInputExpressionFlowValidationDetails) -> dict:
    out: dict = {}
    out["node"] = value["node"]
    out["input"] = value["input"]
    out["cause"] = value["cause"]
    return out


def deserialize_json(data: dict) -> MalformedNodeInputExpressionFlowValidationDetails:
    out: MalformedNodeInputExpressionFlowValidationDetails = {}  # type: ignore[typeddict-item]
    if "node" in data:
        out["node"] = data["node"]
    else:
        raise DeserializationError(
            "MalformedNodeInputExpressionFlowValidationDetails.node required"
        )
    if "input" in data:
        out["input"] = data["input"]
    else:
        raise DeserializationError(
            "MalformedNodeInputExpressionFlowValidationDetails.input required"
        )
    if "cause" in data:
        out["cause"] = data["cause"]
    else:
        raise DeserializationError(
            "MalformedNodeInputExpressionFlowValidationDetails.cause required"
        )
    return out
