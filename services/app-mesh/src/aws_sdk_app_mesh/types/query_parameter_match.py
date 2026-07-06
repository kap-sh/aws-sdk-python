"""Generated from Smithy shape ``com.amazonaws.appmesh#QueryParameterMatch``."""

from typing_extensions import NotRequired, TypedDict


class QueryParameterMatch(TypedDict, closed=True):
    exact: NotRequired["str"]
    """<p>The exact query parameter to match on.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: QueryParameterMatch) -> dict:
    out: dict = {}
    if "exact" in value:
        out["exact"] = value["exact"]
    return out


def deserialize_json(data: dict) -> QueryParameterMatch:
    out: QueryParameterMatch = {}  # type: ignore[typeddict-item]
    if "exact" in data:
        out["exact"] = data["exact"]
    return out
