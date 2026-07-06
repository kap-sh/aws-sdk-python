"""Generated from Smithy shape ``com.amazonaws.neptunedata#ListGremlinQueriesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_neptunedata.types.gremlin_queries


class ListGremlinQueriesOutput(TypedDict, closed=True):
    accepted_query_count: NotRequired["int"]
    """<p>The number of queries that have been accepted but not yet completed, including queries in the queue.</p>"""
    running_query_count: NotRequired["int"]
    """<p>The number of Gremlin queries currently running.</p>"""
    queries: NotRequired["aws_sdk_neptunedata.types.gremlin_queries.GremlinQueries"]
    """<p>A list of the current queries.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListGremlinQueriesOutput) -> dict:
    out: dict = {}
    if "accepted_query_count" in value:
        out["acceptedQueryCount"] = value["accepted_query_count"]
    if "running_query_count" in value:
        out["runningQueryCount"] = value["running_query_count"]
    if "queries" in value:
        import aws_sdk_neptunedata.types.gremlin_queries

        out["queries"] = aws_sdk_neptunedata.types.gremlin_queries.serialize_json(
            value["queries"]
        )
    return out


def deserialize_json(data: dict) -> ListGremlinQueriesOutput:
    out: ListGremlinQueriesOutput = {}  # type: ignore[typeddict-item]
    if "acceptedQueryCount" in data:
        out["accepted_query_count"] = data["acceptedQueryCount"]
    if "runningQueryCount" in data:
        out["running_query_count"] = data["runningQueryCount"]
    if "queries" in data:
        import aws_sdk_neptunedata.types.gremlin_queries

        out["queries"] = aws_sdk_neptunedata.types.gremlin_queries.deserialize_json(
            data["queries"]
        )
    return out
