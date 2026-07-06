"""Generated from Smithy shape ``com.amazonaws.opensearch#NodeOption``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.node_config
    import aws_sdk_opensearch.types.node_options_node_type


class NodeOption(TypedDict, closed=True):
    node_type: NotRequired[
        "aws_sdk_opensearch.types.node_options_node_type.NodeOptionsNodeType"
    ]
    """<p>Defines the type of node, such as coordinating nodes.</p>"""
    node_config: NotRequired["aws_sdk_opensearch.types.node_config.NodeConfig"]
    """<p>Configuration options for defining the setup of any node type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NodeOption) -> dict:
    out: dict = {}
    if "node_type" in value:
        import aws_sdk_opensearch.types.node_options_node_type

        out["NodeType"] = (
            aws_sdk_opensearch.types.node_options_node_type.serialize_json(
                value["node_type"]
            )
        )
    if "node_config" in value:
        import aws_sdk_opensearch.types.node_config

        out["NodeConfig"] = aws_sdk_opensearch.types.node_config.serialize_json(
            value["node_config"]
        )
    return out


def deserialize_json(data: dict) -> NodeOption:
    out: NodeOption = {}  # type: ignore[typeddict-item]
    if "NodeType" in data:
        import aws_sdk_opensearch.types.node_options_node_type

        out["node_type"] = (
            aws_sdk_opensearch.types.node_options_node_type.deserialize_json(
                data["NodeType"]
            )
        )
    if "NodeConfig" in data:
        import aws_sdk_opensearch.types.node_config

        out["node_config"] = aws_sdk_opensearch.types.node_config.deserialize_json(
            data["NodeConfig"]
        )
    return out
