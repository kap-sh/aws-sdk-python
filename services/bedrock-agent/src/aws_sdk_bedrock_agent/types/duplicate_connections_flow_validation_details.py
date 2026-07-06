"""Generated from Smithy shape ``com.amazonaws.bedrockagent#DuplicateConnectionsFlowValidationDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.flow_node_name


class DuplicateConnectionsFlowValidationDetails(TypedDict, closed=True):
    source: "aws_sdk_bedrock_agent.types.flow_node_name.FlowNodeName"
    """<p>The name of the source node where the duplicate connection starts.</p>"""
    target: "aws_sdk_bedrock_agent.types.flow_node_name.FlowNodeName"
    """<p>The name of the target node where the duplicate connection ends.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DuplicateConnectionsFlowValidationDetails) -> dict:
    out: dict = {}
    out["source"] = value["source"]
    out["target"] = value["target"]
    return out


def deserialize_json(data: dict) -> DuplicateConnectionsFlowValidationDetails:
    out: DuplicateConnectionsFlowValidationDetails = {}  # type: ignore[typeddict-item]
    if "source" in data:
        out["source"] = data["source"]
    else:
        raise DeserializationError(
            "DuplicateConnectionsFlowValidationDetails.source required"
        )
    if "target" in data:
        out["target"] = data["target"]
    else:
        raise DeserializationError(
            "DuplicateConnectionsFlowValidationDetails.target required"
        )
    return out
