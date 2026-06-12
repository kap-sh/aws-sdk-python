"""Generated from Smithy shape ``com.amazonaws.sagemaker#QueryLineageResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.edges
    import aws_sdk_sagemaker.types.string8192
    import aws_sdk_sagemaker.types.vertices


class QueryLineageResponse(TypedDict):
    vertices: NotRequired["aws_sdk_sagemaker.types.vertices.Vertices"]
    """<p>A list of vertices connected to the start entity(ies) in the lineage graph.</p>"""
    edges: NotRequired["aws_sdk_sagemaker.types.edges.Edges"]
    """<p>A list of edges that connect vertices in the response.</p>"""
    next_token: NotRequired["aws_sdk_sagemaker.types.string8192.String8192"]
    """<p>Limits the number of vertices in the response. Use the <code>NextToken</code> in a response to to retrieve the next page of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: QueryLineageResponse) -> dict:
    out: dict = {}
    if "vertices" in value:
        import aws_sdk_sagemaker.types.vertices

        out["Vertices"] = aws_sdk_sagemaker.types.vertices.serialize_aws_json_1_1(
            value["vertices"]
        )
    if "edges" in value:
        import aws_sdk_sagemaker.types.edges

        out["Edges"] = aws_sdk_sagemaker.types.edges.serialize_aws_json_1_1(
            value["edges"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> QueryLineageResponse:
    out: QueryLineageResponse = {}  # type: ignore[typeddict-item]
    if "Vertices" in data:
        import aws_sdk_sagemaker.types.vertices

        out["vertices"] = aws_sdk_sagemaker.types.vertices.deserialize_aws_json_1_1(
            data["Vertices"]
        )
    if "Edges" in data:
        import aws_sdk_sagemaker.types.edges

        out["edges"] = aws_sdk_sagemaker.types.edges.deserialize_aws_json_1_1(
            data["Edges"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
