"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#RetrievalResultSqlLocation``."""

from typing_extensions import NotRequired, TypedDict


class RetrievalResultSqlLocation(TypedDict, closed=True):
    query: NotRequired["str"]
    """<p>The SQL query used to retrieve the result.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RetrievalResultSqlLocation) -> dict:
    out: dict = {}
    if "query" in value:
        out["query"] = value["query"]
    return out


def deserialize_json(data: dict) -> RetrievalResultSqlLocation:
    out: RetrievalResultSqlLocation = {}  # type: ignore[typeddict-item]
    if data.get("query") is not None:
        out["query"] = data["query"]
    return out
