"""Generated from Smithy shape ``com.amazonaws.rtbfabric#QueryStringKeyValuePair``."""

from typing_extensions import TypedDict

from capo_rtbfabric.errors import DeserializationError


class QueryStringKeyValuePair(TypedDict, closed=True):
    key: "str"
    """<p>The key of the query string parameter to match. Must contain only RFC 3986 unreserved characters.</p>"""
    value: "str"
    """<p>The value of the query string parameter to match. Must contain only RFC 3986 unreserved characters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: QueryStringKeyValuePair) -> dict:
    out: dict = {}
    out["key"] = value["key"]
    out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> QueryStringKeyValuePair:
    out: QueryStringKeyValuePair = {}  # type: ignore[typeddict-item]
    if "key" in data:
        out["key"] = data["key"]
    else:
        raise DeserializationError("QueryStringKeyValuePair.key required")
    if "value" in data:
        out["value"] = data["value"]
    else:
        raise DeserializationError("QueryStringKeyValuePair.value required")
    return out
