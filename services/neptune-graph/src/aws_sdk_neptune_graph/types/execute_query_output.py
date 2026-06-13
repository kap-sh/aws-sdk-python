"""Generated from Smithy shape ``com.amazonaws.neptunegraph#ExecuteQueryOutput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_neptune_graph.types.query_response_blob


class ExecuteQueryOutput(TypedDict):
    payload: "aws_sdk_neptune_graph.types.query_response_blob.QueryResponseBlob"
    """<p>The query results.</p>"""
