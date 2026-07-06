"""Generated from Smithy shape ``com.amazonaws.glue#GetDataflowGraphResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.dag_edges
    import aws_sdk_glue.types.dag_nodes


class GetDataflowGraphResponse(TypedDict, closed=True):
    dag_nodes: NotRequired["aws_sdk_glue.types.dag_nodes.DagNodes"]
    """<p>A list of the nodes in the resulting DAG.</p>"""
    dag_edges: NotRequired["aws_sdk_glue.types.dag_edges.DagEdges"]
    """<p>A list of the edges in the resulting DAG.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetDataflowGraphResponse) -> dict:
    out: dict = {}
    if "dag_nodes" in value:
        import aws_sdk_glue.types.dag_nodes

        out["DagNodes"] = aws_sdk_glue.types.dag_nodes.serialize_aws_json_1_1(
            value["dag_nodes"]
        )
    if "dag_edges" in value:
        import aws_sdk_glue.types.dag_edges

        out["DagEdges"] = aws_sdk_glue.types.dag_edges.serialize_aws_json_1_1(
            value["dag_edges"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetDataflowGraphResponse:
    out: GetDataflowGraphResponse = {}  # type: ignore[typeddict-item]
    if "DagNodes" in data:
        import aws_sdk_glue.types.dag_nodes

        out["dag_nodes"] = aws_sdk_glue.types.dag_nodes.deserialize_aws_json_1_1(
            data["DagNodes"]
        )
    if "DagEdges" in data:
        import aws_sdk_glue.types.dag_edges

        out["dag_edges"] = aws_sdk_glue.types.dag_edges.deserialize_aws_json_1_1(
            data["DagEdges"]
        )
    return out
