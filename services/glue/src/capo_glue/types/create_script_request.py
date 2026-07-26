"""Generated from Smithy shape ``com.amazonaws.glue#CreateScriptRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.dag_edges
    import capo_glue.types.dag_nodes
    import capo_glue.types.language


class CreateScriptRequest(TypedDict, closed=True):
    dag_nodes: NotRequired["capo_glue.types.dag_nodes.DagNodes"]
    """<p>A list of the nodes in the DAG.</p>"""
    dag_edges: NotRequired["capo_glue.types.dag_edges.DagEdges"]
    """<p>A list of the edges in the DAG.</p>"""
    language: NotRequired["capo_glue.types.language.Language"]
    """<p>The programming language of the resulting code from the DAG.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateScriptRequest) -> dict:
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
    if "language" in value:
        import capo_glue.types.language

        out["Language"] = capo_glue.types.language.serialize_aws_json_1_1(
            value["language"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateScriptRequest:
    out: CreateScriptRequest = {}  # type: ignore[typeddict-item]
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
    if "Language" in data:
        import capo_glue.types.language

        out["language"] = capo_glue.types.language.deserialize_aws_json_1_1(
            data["Language"]
        )
    return out
