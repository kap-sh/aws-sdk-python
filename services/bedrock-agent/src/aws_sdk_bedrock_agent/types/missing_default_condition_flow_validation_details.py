"""Generated from Smithy shape ``com.amazonaws.bedrockagent#MissingDefaultConditionFlowValidationDetails``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.flow_node_name


class MissingDefaultConditionFlowValidationDetails(TypedDict):
    node: "aws_sdk_bedrock_agent.types.flow_node_name.FlowNodeName"
    """<p>The name of the node missing the default condition.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MissingDefaultConditionFlowValidationDetails) -> dict:
    out: dict = {}
    out["node"] = value["node"]
    return out


def deserialize_json(data: dict) -> MissingDefaultConditionFlowValidationDetails:
    out: MissingDefaultConditionFlowValidationDetails = {}  # type: ignore[typeddict-item]
    if "node" in data:
        out["node"] = data["node"]
    else:
        raise DeserializationError(
            "MissingDefaultConditionFlowValidationDetails.node required"
        )
    return out
