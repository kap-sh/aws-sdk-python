"""Generated from Smithy shape ``com.amazonaws.neptunedata#ListOpenCypherQueriesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_neptunedata.types.open_cypher_queries


class ListOpenCypherQueriesOutput(TypedDict, closed=True):
    accepted_query_count: NotRequired["int"]
    """<p>The number of queries that have been accepted but not yet completed, including queries in the queue.</p>"""
    running_query_count: NotRequired["int"]
    """<p>The number of currently running openCypher queries.</p>"""
    queries: NotRequired["capo_neptunedata.types.open_cypher_queries.OpenCypherQueries"]
    """<p>A list of current openCypher queries.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListOpenCypherQueriesOutput) -> dict:
    out: dict = {}
    if "accepted_query_count" in value:
        out["acceptedQueryCount"] = value["accepted_query_count"]
    if "running_query_count" in value:
        out["runningQueryCount"] = value["running_query_count"]
    if "queries" in value:
        import capo_neptunedata.types.open_cypher_queries

        out["queries"] = capo_neptunedata.types.open_cypher_queries.serialize_json(
            value["queries"]
        )
    return out


def deserialize_json(data: dict) -> ListOpenCypherQueriesOutput:
    out: ListOpenCypherQueriesOutput = {}  # type: ignore[typeddict-item]
    if "acceptedQueryCount" in data:
        out["accepted_query_count"] = data["acceptedQueryCount"]
    if "runningQueryCount" in data:
        out["running_query_count"] = data["runningQueryCount"]
    if "queries" in data:
        import capo_neptunedata.types.open_cypher_queries

        out["queries"] = capo_neptunedata.types.open_cypher_queries.deserialize_json(
            data["queries"]
        )
    return out
