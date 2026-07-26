"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#NodeInputExecutionChainItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agent_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.flow_control_node_type
    import capo_bedrock_agent_runtime.types.node_name


class NodeInputExecutionChainItem(TypedDict, closed=True):
    node_name: "capo_bedrock_agent_runtime.types.node_name.NodeName"
    """<p>The name of the node in the execution chain.</p>"""
    index: NotRequired["int"]
    """<p>The index position of this item in the execution chain.</p>"""
    type: "capo_bedrock_agent_runtime.types.flow_control_node_type.FlowControlNodeType"
    """<p>The type of execution chain item. Supported values are Iterator and Loop.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NodeInputExecutionChainItem) -> dict:
    out: dict = {}
    out["nodeName"] = value["node_name"]
    if "index" in value:
        out["index"] = value["index"]
    import capo_bedrock_agent_runtime.types.flow_control_node_type

    out["type"] = (
        capo_bedrock_agent_runtime.types.flow_control_node_type.serialize_json(
            value["type"]
        )
    )
    return out


def deserialize_json(data: dict) -> NodeInputExecutionChainItem:
    out: NodeInputExecutionChainItem = {}  # type: ignore[typeddict-item]
    if "nodeName" in data:
        out["node_name"] = data["nodeName"]
    else:
        raise DeserializationError("NodeInputExecutionChainItem.node_name required")
    if "index" in data:
        out["index"] = data["index"]
    if "type" in data:
        import capo_bedrock_agent_runtime.types.flow_control_node_type

        out["type"] = (
            capo_bedrock_agent_runtime.types.flow_control_node_type.deserialize_json(
                data["type"]
            )
        )
    else:
        raise DeserializationError("NodeInputExecutionChainItem.type required")
    return out
