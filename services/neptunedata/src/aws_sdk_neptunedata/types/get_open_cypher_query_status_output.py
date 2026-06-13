"""Generated from Smithy shape ``com.amazonaws.neptunedata#GetOpenCypherQueryStatusOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_neptunedata.types.query_eval_stats


class GetOpenCypherQueryStatusOutput(TypedDict):
    query_id: NotRequired["str"]
    """<p>The unique ID of the query for which status is being returned.</p>"""
    query_string: NotRequired["str"]
    """<p>The openCypher query string.</p>"""
    query_eval_stats: NotRequired[
        "aws_sdk_neptunedata.types.query_eval_stats.QueryEvalStats"
    ]
    """<p>The openCypher query evaluation status.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetOpenCypherQueryStatusOutput) -> dict:
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


def deserialize_json(data: dict) -> GetOpenCypherQueryStatusOutput:
    out: GetOpenCypherQueryStatusOutput = {}  # type: ignore[typeddict-item]
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
