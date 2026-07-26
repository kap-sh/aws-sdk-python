"""Generated from Smithy shape ``com.amazonaws.glue#WorkflowGraph``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.edge_list
    import capo_glue.types.node_list


class WorkflowGraph(TypedDict, closed=True):
    nodes: NotRequired["capo_glue.types.node_list.NodeList"]
    """<p>A list of the the Glue components belong to the workflow represented as nodes.</p>"""
    edges: NotRequired["capo_glue.types.edge_list.EdgeList"]
    """<p>A list of all the directed connections between the nodes belonging to the workflow.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WorkflowGraph) -> dict:
    out: dict = {}
    if "nodes" in value:
        import capo_glue.types.node_list

        out["Nodes"] = capo_glue.types.node_list.serialize_aws_json_1_1(value["nodes"])
    if "edges" in value:
        import capo_glue.types.edge_list

        out["Edges"] = capo_glue.types.edge_list.serialize_aws_json_1_1(value["edges"])
    return out


def deserialize_aws_json_1_1(data: dict) -> WorkflowGraph:
    out: WorkflowGraph = {}  # type: ignore[typeddict-item]
    if "Nodes" in data:
        import capo_glue.types.node_list

        out["nodes"] = capo_glue.types.node_list.deserialize_aws_json_1_1(data["Nodes"])
    if "Edges" in data:
        import capo_glue.types.edge_list

        out["edges"] = capo_glue.types.edge_list.deserialize_aws_json_1_1(data["Edges"])
    return out
