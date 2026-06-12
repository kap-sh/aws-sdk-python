"""Generated from Smithy shape ``com.amazonaws.glue#CreateScriptRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.dag_edges
    import aws_sdk_glue.types.dag_nodes
    import aws_sdk_glue.types.language


class CreateScriptRequest(TypedDict):
    dag_nodes: NotRequired["aws_sdk_glue.types.dag_nodes.DagNodes"]
    """<p>A list of the nodes in the DAG.</p>"""
    dag_edges: NotRequired["aws_sdk_glue.types.dag_edges.DagEdges"]
    """<p>A list of the edges in the DAG.</p>"""
    language: NotRequired["aws_sdk_glue.types.language.Language"]
    """<p>The programming language of the resulting code from the DAG.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateScriptRequest) -> dict:
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
    if "language" in value:
        import aws_sdk_glue.types.language

        out["Language"] = aws_sdk_glue.types.language.serialize_aws_json_1_1(
            value["language"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateScriptRequest:
    out: CreateScriptRequest = {}  # type: ignore[typeddict-item]
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
    if "Language" in data:
        import aws_sdk_glue.types.language

        out["language"] = aws_sdk_glue.types.language.deserialize_aws_json_1_1(
            data["Language"]
        )
    return out
