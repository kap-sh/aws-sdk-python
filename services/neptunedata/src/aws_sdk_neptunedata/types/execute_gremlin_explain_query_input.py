"""Generated from Smithy shape ``com.amazonaws.neptunedata#ExecuteGremlinExplainQueryInput``."""

from typing import TypedDict
from aws_sdk_neptunedata.errors import DeserializationError

class ExecuteGremlinExplainQueryInput(TypedDict):
    gremlin_query: "str"
    """<p>The Gremlin explain query string.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: ExecuteGremlinExplainQueryInput) -> dict:
    out: dict = {}
    out["gremlin"] = value["gremlin_query"]
    return out


def deserialize_json(data: dict) -> ExecuteGremlinExplainQueryInput:
    out: ExecuteGremlinExplainQueryInput = {}  # type: ignore[typeddict-item]
    if "gremlin" in data:
        out["gremlin_query"] = data["gremlin"]
    else:
        raise DeserializationError("ExecuteGremlinExplainQueryInput.gremlin_query required")
    return out