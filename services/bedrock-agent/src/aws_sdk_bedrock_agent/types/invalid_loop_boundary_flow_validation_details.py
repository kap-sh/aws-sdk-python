"""Generated from Smithy shape ``com.amazonaws.bedrockagent#InvalidLoopBoundaryFlowValidationDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.flow_connection_name
    import aws_sdk_bedrock_agent.types.flow_node_name


class InvalidLoopBoundaryFlowValidationDetails(TypedDict, closed=True):
    connection: "aws_sdk_bedrock_agent.types.flow_connection_name.FlowConnectionName"
    """<p>The name of the connection that violates loop boundary rules.</p>"""
    source: "aws_sdk_bedrock_agent.types.flow_node_name.FlowNodeName"
    """<p>The source node of the connection that violates DoWhile loop boundary rules.</p>"""
    target: "aws_sdk_bedrock_agent.types.flow_node_name.FlowNodeName"
    """<p>The target node of the connection that violates DoWhile loop boundary rules.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InvalidLoopBoundaryFlowValidationDetails) -> dict:
    out: dict = {}
    out["connection"] = value["connection"]
    out["source"] = value["source"]
    out["target"] = value["target"]
    return out


def deserialize_json(data: dict) -> InvalidLoopBoundaryFlowValidationDetails:
    out: InvalidLoopBoundaryFlowValidationDetails = {}  # type: ignore[typeddict-item]
    if "connection" in data:
        out["connection"] = data["connection"]
    else:
        raise DeserializationError(
            "InvalidLoopBoundaryFlowValidationDetails.connection required"
        )
    if "source" in data:
        out["source"] = data["source"]
    else:
        raise DeserializationError(
            "InvalidLoopBoundaryFlowValidationDetails.source required"
        )
    if "target" in data:
        out["target"] = data["target"]
    else:
        raise DeserializationError(
            "InvalidLoopBoundaryFlowValidationDetails.target required"
        )
    return out
