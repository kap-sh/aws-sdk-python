"""Generated from Smithy shape ``com.amazonaws.batch#NodeProperties``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_batch.types.integer
    import aws_sdk_batch.types.node_range_properties


class NodeProperties(TypedDict):
    num_nodes: NotRequired["aws_sdk_batch.types.integer.Integer"]
    """<p>The number of nodes that are associated with a multi-node parallel job.</p>"""
    main_node: NotRequired["aws_sdk_batch.types.integer.Integer"]
    """<p>Specifies the node index for the main node of a multi-node parallel job. This node index value must be fewer than the number of nodes.</p>"""
    node_range_properties: NotRequired[
        "aws_sdk_batch.types.node_range_properties.NodeRangeProperties"
    ]
    """<p>A list of node ranges and their properties that are associated with a multi-node parallel job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NodeProperties) -> dict:
    out: dict = {}
    if "num_nodes" in value:
        out["numNodes"] = value["num_nodes"]
    if "main_node" in value:
        out["mainNode"] = value["main_node"]
    if "node_range_properties" in value:
        import aws_sdk_batch.types.node_range_properties

        out["nodeRangeProperties"] = (
            aws_sdk_batch.types.node_range_properties.serialize_json(
                value["node_range_properties"]
            )
        )
    return out


def deserialize_json(data: dict) -> NodeProperties:
    out: NodeProperties = {}  # type: ignore[typeddict-item]
    if "numNodes" in data:
        out["num_nodes"] = data["numNodes"]
    if "mainNode" in data:
        out["main_node"] = data["mainNode"]
    if "nodeRangeProperties" in data:
        import aws_sdk_batch.types.node_range_properties

        out["node_range_properties"] = (
            aws_sdk_batch.types.node_range_properties.deserialize_json(
                data["nodeRangeProperties"]
            )
        )
    return out
