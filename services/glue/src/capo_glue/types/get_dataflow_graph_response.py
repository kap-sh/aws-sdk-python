"""Generated from Smithy shape ``com.amazonaws.glue#GetDataflowGraphResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.dag_edges
    import capo_glue.types.dag_nodes


class GetDataflowGraphResponse(TypedDict, closed=True):
    dag_nodes: NotRequired["capo_glue.types.dag_nodes.DagNodes"]
    """<p>A list of the nodes in the resulting DAG.</p>"""
    dag_edges: NotRequired["capo_glue.types.dag_edges.DagEdges"]
    """<p>A list of the edges in the resulting DAG.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetDataflowGraphResponse) -> dict:
    out: dict = {}
    if "dag_nodes" in value:
        import capo_glue.types.dag_nodes

        out["DagNodes"] = capo_glue.types.dag_nodes.serialize_aws_json_1_1(
            value["dag_nodes"]
        )
    if "dag_edges" in value:
        import capo_glue.types.dag_edges

        out["DagEdges"] = capo_glue.types.dag_edges.serialize_aws_json_1_1(
            value["dag_edges"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetDataflowGraphResponse:
    out: GetDataflowGraphResponse = {}  # type: ignore[typeddict-item]
    if "DagNodes" in data:
        import capo_glue.types.dag_nodes

        out["dag_nodes"] = capo_glue.types.dag_nodes.deserialize_aws_json_1_1(
            data["DagNodes"]
        )
    if "DagEdges" in data:
        import capo_glue.types.dag_edges

        out["dag_edges"] = capo_glue.types.dag_edges.deserialize_aws_json_1_1(
            data["DagEdges"]
        )
    return out
