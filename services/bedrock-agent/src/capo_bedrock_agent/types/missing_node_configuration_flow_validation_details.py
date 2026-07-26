"""Generated from Smithy shape ``com.amazonaws.bedrockagent#MissingNodeConfigurationFlowValidationDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent.types.flow_node_name


class MissingNodeConfigurationFlowValidationDetails(TypedDict, closed=True):
    node: "capo_bedrock_agent.types.flow_node_name.FlowNodeName"
    """<p>The name of the node missing a required configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MissingNodeConfigurationFlowValidationDetails) -> dict:
    out: dict = {}
    out["node"] = value["node"]
    return out


def deserialize_json(data: dict) -> MissingNodeConfigurationFlowValidationDetails:
    out: MissingNodeConfigurationFlowValidationDetails = {}  # type: ignore[typeddict-item]
    if "node" in data:
        out["node"] = data["node"]
    else:
        raise DeserializationError(
            "MissingNodeConfigurationFlowValidationDetails.node required"
        )
    return out
