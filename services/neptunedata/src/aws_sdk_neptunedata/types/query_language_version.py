"""Generated from Smithy shape ``com.amazonaws.neptunedata#QueryLanguageVersion``."""

from typing import TypedDict

from aws_sdk_neptunedata.errors import DeserializationError


class QueryLanguageVersion(TypedDict):
    version: "str"
    """<p>The version of the query language.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: QueryLanguageVersion) -> dict:
    out: dict = {}
    out["version"] = value["version"]
    return out


def deserialize_json(data: dict) -> QueryLanguageVersion:
    out: QueryLanguageVersion = {}  # type: ignore[typeddict-item]
    if "version" in data:
        out["version"] = data["version"]
    else:
        raise DeserializationError("QueryLanguageVersion.version required")
    return out
