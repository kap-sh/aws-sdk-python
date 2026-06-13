"""Generated from Smithy shape ``com.amazonaws.neptunedata#ExecuteGremlinProfileQueryInput``."""

from typing import TypedDict

from typing_extensions import NotRequired

from aws_sdk_neptunedata.errors import DeserializationError


class ExecuteGremlinProfileQueryInput(TypedDict):
    gremlin_query: "str"
    """<p>The Gremlin query string to profile.</p>"""
    results: NotRequired["bool"]
    """<p>If this flag is set to <code>TRUE</code>, the query results are gathered and displayed as part of the profile report. If <code>FALSE</code>, only the result count is displayed.</p>"""
    chop: NotRequired["int"]
    """<p>If non-zero, causes the results string to be truncated at that number of characters. If set to zero, the string contains all the results.</p>"""
    serializer: NotRequired["str"]
    """<p>If non-null, the gathered results are returned in a serialized response message in the format specified by this parameter. See <a href=\"https://docs.aws.amazon.com/neptune/latest/userguide/gremlin-profile-api.html\">Gremlin profile API in Neptune</a> for more information.</p>"""
    index_ops: NotRequired["bool"]
    """<p>If this flag is set to <code>TRUE</code>, the results include a detailed report of all index operations that took place during query execution and serialization.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExecuteGremlinProfileQueryInput) -> dict:
    out: dict = {}
    out["gremlin"] = value["gremlin_query"]
    if "results" in value:
        out["profile.results"] = value["results"]
    if "chop" in value:
        out["profile.chop"] = value["chop"]
    if "serializer" in value:
        out["profile.serializer"] = value["serializer"]
    if "index_ops" in value:
        out["profile.indexOps"] = value["index_ops"]
    return out


def deserialize_json(data: dict) -> ExecuteGremlinProfileQueryInput:
    out: ExecuteGremlinProfileQueryInput = {}  # type: ignore[typeddict-item]
    if "gremlin" in data:
        out["gremlin_query"] = data["gremlin"]
    else:
        raise DeserializationError(
            "ExecuteGremlinProfileQueryInput.gremlin_query required"
        )
    if "profile.results" in data:
        out["results"] = data["profile.results"]
    if "profile.chop" in data:
        out["chop"] = data["profile.chop"]
    if "profile.serializer" in data:
        out["serializer"] = data["profile.serializer"]
    if "profile.indexOps" in data:
        out["index_ops"] = data["profile.indexOps"]
    return out
