"""Generated from Smithy shape ``com.amazonaws.bedrockagent#MissingLoopControllerNodeFlowValidationDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.flow_node_name


class MissingLoopControllerNodeFlowValidationDetails(TypedDict, closed=True):
    loop_node: "aws_sdk_bedrock_agent.types.flow_node_name.FlowNodeName"
    """<p>The DoWhile loop in a flow that's missing a required <code>LoopController</code> node.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MissingLoopControllerNodeFlowValidationDetails) -> dict:
    out: dict = {}
    out["loopNode"] = value["loop_node"]
    return out


def deserialize_json(data: dict) -> MissingLoopControllerNodeFlowValidationDetails:
    out: MissingLoopControllerNodeFlowValidationDetails = {}  # type: ignore[typeddict-item]
    if "loopNode" in data:
        out["loop_node"] = data["loopNode"]
    else:
        raise DeserializationError(
            "MissingLoopControllerNodeFlowValidationDetails.loop_node required"
        )
    return out
