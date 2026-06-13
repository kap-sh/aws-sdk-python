"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#RetrievalResultSqlLocation``."""

from typing import TypedDict

from typing_extensions import NotRequired


class RetrievalResultSqlLocation(TypedDict):
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
    if "query" in data:
        out["query"] = data["query"]
    return out
