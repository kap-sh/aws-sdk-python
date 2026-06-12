"""Generated from Smithy shape ``com.amazonaws.bedrockagent#MismatchedNodeInputTypeFlowValidationDetails``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.flow_node_input_name
    import aws_sdk_bedrock_agent.types.flow_node_io_data_type
    import aws_sdk_bedrock_agent.types.flow_node_name


class MismatchedNodeInputTypeFlowValidationDetails(TypedDict):
    node: "aws_sdk_bedrock_agent.types.flow_node_name.FlowNodeName"
    """<p>The name of the node containing the input with the mismatched data type.</p>"""
    input: "aws_sdk_bedrock_agent.types.flow_node_input_name.FlowNodeInputName"
    """<p>The name of the input with the mismatched data type.</p>"""
    expected_type: (
        "aws_sdk_bedrock_agent.types.flow_node_io_data_type.FlowNodeIODataType"
    )
    """<p>The expected data type for the node input.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MismatchedNodeInputTypeFlowValidationDetails) -> dict:
    out: dict = {}
    out["node"] = value["node"]
    out["input"] = value["input"]
    import aws_sdk_bedrock_agent.types.flow_node_io_data_type

    out["expectedType"] = (
        aws_sdk_bedrock_agent.types.flow_node_io_data_type.serialize_json(
            value["expected_type"]
        )
    )
    return out


def deserialize_json(data: dict) -> MismatchedNodeInputTypeFlowValidationDetails:
    out: MismatchedNodeInputTypeFlowValidationDetails = {}  # type: ignore[typeddict-item]
    if "node" in data:
        out["node"] = data["node"]
    else:
        raise DeserializationError(
            "MismatchedNodeInputTypeFlowValidationDetails.node required"
        )
    if "input" in data:
        out["input"] = data["input"]
    else:
        raise DeserializationError(
            "MismatchedNodeInputTypeFlowValidationDetails.input required"
        )
    if "expectedType" in data:
        import aws_sdk_bedrock_agent.types.flow_node_io_data_type

        out["expected_type"] = (
            aws_sdk_bedrock_agent.types.flow_node_io_data_type.deserialize_json(
                data["expectedType"]
            )
        )
    else:
        raise DeserializationError(
            "MismatchedNodeInputTypeFlowValidationDetails.expected_type required"
        )
    return out
