"""Generated from Smithy shape ``com.amazonaws.neptunegraph#ExecuteQueryOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_neptune_graph.types.query_response_blob


class ExecuteQueryOutput(TypedDict, closed=True):
    payload: "capo_neptune_graph.types.query_response_blob.QueryResponseBlob"
    """<p>The query results.</p>"""
