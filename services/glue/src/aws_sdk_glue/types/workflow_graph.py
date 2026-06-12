"""Generated from Smithy shape ``com.amazonaws.glue#WorkflowGraph``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.edge_list
    import aws_sdk_glue.types.node_list


class WorkflowGraph(TypedDict):
    nodes: NotRequired["aws_sdk_glue.types.node_list.NodeList"]
    """<p>A list of the the Glue components belong to the workflow represented as nodes.</p>"""
    edges: NotRequired["aws_sdk_glue.types.edge_list.EdgeList"]
    """<p>A list of all the directed connections between the nodes belonging to the workflow.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WorkflowGraph) -> dict:
    out: dict = {}
    if "nodes" in value:
        import aws_sdk_glue.types.node_list

        out["Nodes"] = aws_sdk_glue.types.node_list.serialize_aws_json_1_1(
            value["nodes"]
        )
    if "edges" in value:
        import aws_sdk_glue.types.edge_list

        out["Edges"] = aws_sdk_glue.types.edge_list.serialize_aws_json_1_1(
            value["edges"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> WorkflowGraph:
    out: WorkflowGraph = {}  # type: ignore[typeddict-item]
    if "Nodes" in data:
        import aws_sdk_glue.types.node_list

        out["nodes"] = aws_sdk_glue.types.node_list.deserialize_aws_json_1_1(
            data["Nodes"]
        )
    if "Edges" in data:
        import aws_sdk_glue.types.edge_list

        out["edges"] = aws_sdk_glue.types.edge_list.deserialize_aws_json_1_1(
            data["Edges"]
        )
    return out
