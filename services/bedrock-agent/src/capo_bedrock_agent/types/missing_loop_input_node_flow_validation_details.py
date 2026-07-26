"""Generated from Smithy shape ``com.amazonaws.bedrockagent#MissingLoopInputNodeFlowValidationDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent.types.flow_node_name


class MissingLoopInputNodeFlowValidationDetails(TypedDict, closed=True):
    loop_node: "capo_bedrock_agent.types.flow_node_name.FlowNodeName"
    """<p>The DoWhile loop in a flow that's missing a required <code>LoopInput</code> node.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MissingLoopInputNodeFlowValidationDetails) -> dict:
    out: dict = {}
    out["loopNode"] = value["loop_node"]
    return out


def deserialize_json(data: dict) -> MissingLoopInputNodeFlowValidationDetails:
    out: MissingLoopInputNodeFlowValidationDetails = {}  # type: ignore[typeddict-item]
    if "loopNode" in data:
        out["loop_node"] = data["loopNode"]
    else:
        raise DeserializationError(
            "MissingLoopInputNodeFlowValidationDetails.loop_node required"
        )
    return out
