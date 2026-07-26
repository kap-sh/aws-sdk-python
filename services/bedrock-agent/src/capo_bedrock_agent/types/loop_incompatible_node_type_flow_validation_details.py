"""Generated from Smithy shape ``com.amazonaws.bedrockagent#LoopIncompatibleNodeTypeFlowValidationDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent.types.flow_node_name
    import capo_bedrock_agent.types.incompatible_loop_node_type


class LoopIncompatibleNodeTypeFlowValidationDetails(TypedDict, closed=True):
    node: "capo_bedrock_agent.types.flow_node_name.FlowNodeName"
    """<p>The <code>Loop</code> container node that contains an incompatible node.</p>"""
    incompatible_node_type: (
        "capo_bedrock_agent.types.incompatible_loop_node_type.IncompatibleLoopNodeType"
    )
    """<p>The node type of the incompatible node in the DoWhile loop. Some node types, like a condition node, aren't allowed in a DoWhile loop.</p>"""
    incompatible_node_name: "capo_bedrock_agent.types.flow_node_name.FlowNodeName"
    """<p>The node that's incompatible in the DoWhile loop.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LoopIncompatibleNodeTypeFlowValidationDetails) -> dict:
    out: dict = {}
    out["node"] = value["node"]
    import capo_bedrock_agent.types.incompatible_loop_node_type

    out["incompatibleNodeType"] = (
        capo_bedrock_agent.types.incompatible_loop_node_type.serialize_json(
            value["incompatible_node_type"]
        )
    )
    out["incompatibleNodeName"] = value["incompatible_node_name"]
    return out


def deserialize_json(data: dict) -> LoopIncompatibleNodeTypeFlowValidationDetails:
    out: LoopIncompatibleNodeTypeFlowValidationDetails = {}  # type: ignore[typeddict-item]
    if "node" in data:
        out["node"] = data["node"]
    else:
        raise DeserializationError(
            "LoopIncompatibleNodeTypeFlowValidationDetails.node required"
        )
    if "incompatibleNodeType" in data:
        import capo_bedrock_agent.types.incompatible_loop_node_type

        out["incompatible_node_type"] = (
            capo_bedrock_agent.types.incompatible_loop_node_type.deserialize_json(
                data["incompatibleNodeType"]
            )
        )
    else:
        raise DeserializationError(
            "LoopIncompatibleNodeTypeFlowValidationDetails.incompatible_node_type required"
        )
    if "incompatibleNodeName" in data:
        out["incompatible_node_name"] = data["incompatibleNodeName"]
    else:
        raise DeserializationError(
            "LoopIncompatibleNodeTypeFlowValidationDetails.incompatible_node_name required"
        )
    return out
