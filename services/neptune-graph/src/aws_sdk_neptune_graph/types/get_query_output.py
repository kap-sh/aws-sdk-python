"""Generated from Smithy shape ``com.amazonaws.neptunegraph#GetQueryOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_neptune_graph.types.query_state


class GetQueryOutput(TypedDict, closed=True):
    id: NotRequired["str"]
    """<p>The ID of the query in question.</p>"""
    query_string: NotRequired["str"]
    """<p>The query in question.</p>"""
    waited: NotRequired["int"]
    """<p>Indicates how long the query waited, in milliseconds.</p>"""
    elapsed: NotRequired["int"]
    """<p>The number of milliseconds the query has been running.</p>"""
    state: NotRequired["aws_sdk_neptune_graph.types.query_state.QueryState"]
    """<p>State of the query.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetQueryOutput) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "query_string" in value:
        out["queryString"] = value["query_string"]
    if "waited" in value:
        out["waited"] = value["waited"]
    if "elapsed" in value:
        out["elapsed"] = value["elapsed"]
    if "state" in value:
        import aws_sdk_neptune_graph.types.query_state

        out["state"] = aws_sdk_neptune_graph.types.query_state.serialize_json(
            value["state"]
        )
    return out


def deserialize_json(data: dict) -> GetQueryOutput:
    out: GetQueryOutput = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "queryString" in data:
        out["query_string"] = data["queryString"]
    if "waited" in data:
        out["waited"] = data["waited"]
    if "elapsed" in data:
        out["elapsed"] = data["elapsed"]
    if "state" in data:
        import aws_sdk_neptune_graph.types.query_state

        out["state"] = aws_sdk_neptune_graph.types.query_state.deserialize_json(
            data["state"]
        )
    return out
