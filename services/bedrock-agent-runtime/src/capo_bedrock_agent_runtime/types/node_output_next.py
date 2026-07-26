"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#NodeOutputNext``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock_agent_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.flow_node_input_name
    import capo_bedrock_agent_runtime.types.node_name


class NodeOutputNext(TypedDict, closed=True):
    node_name: "capo_bedrock_agent_runtime.types.node_name.NodeName"
    """<p>The name of the next node that receives the output data.</p>"""
    input_field_name: (
        "capo_bedrock_agent_runtime.types.flow_node_input_name.FlowNodeInputName"
    )
    """<p>The name of the input field in the next node that receives the data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NodeOutputNext) -> dict:
    out: dict = {}
    out["nodeName"] = value["node_name"]
    out["inputFieldName"] = value["input_field_name"]
    return out


def deserialize_json(data: dict) -> NodeOutputNext:
    out: NodeOutputNext = {}  # type: ignore[typeddict-item]
    if "nodeName" in data:
        out["node_name"] = data["nodeName"]
    else:
        raise DeserializationError("NodeOutputNext.node_name required")
    if "inputFieldName" in data:
        out["input_field_name"] = data["inputFieldName"]
    else:
        raise DeserializationError("NodeOutputNext.input_field_name required")
    return out
