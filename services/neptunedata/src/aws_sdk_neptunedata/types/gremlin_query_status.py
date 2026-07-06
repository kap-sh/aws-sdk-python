"""Generated from Smithy shape ``com.amazonaws.neptunedata#GremlinQueryStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_neptunedata.types.query_eval_stats


class GremlinQueryStatus(TypedDict, closed=True):
    query_id: NotRequired["str"]
    """<p>The ID of the Gremlin query.</p>"""
    query_string: NotRequired["str"]
    """<p>The query string of the Gremlin query.</p>"""
    query_eval_stats: NotRequired[
        "aws_sdk_neptunedata.types.query_eval_stats.QueryEvalStats"
    ]
    """<p>The query statistics of the Gremlin query.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GremlinQueryStatus) -> dict:
    out: dict = {}
    if "query_id" in value:
        out["queryId"] = value["query_id"]
    if "query_string" in value:
        out["queryString"] = value["query_string"]
    if "query_eval_stats" in value:
        import aws_sdk_neptunedata.types.query_eval_stats

        out["queryEvalStats"] = (
            aws_sdk_neptunedata.types.query_eval_stats.serialize_json(
                value["query_eval_stats"]
            )
        )
    return out


def deserialize_json(data: dict) -> GremlinQueryStatus:
    out: GremlinQueryStatus = {}  # type: ignore[typeddict-item]
    if "queryId" in data:
        out["query_id"] = data["queryId"]
    if "queryString" in data:
        out["query_string"] = data["queryString"]
    if "queryEvalStats" in data:
        import aws_sdk_neptunedata.types.query_eval_stats

        out["query_eval_stats"] = (
            aws_sdk_neptunedata.types.query_eval_stats.deserialize_json(
                data["queryEvalStats"]
            )
        )
    return out
