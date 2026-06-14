"""Generated from Smithy shape ``com.amazonaws.neptunedata#SparqlData``."""

from typing import TypedDict

from aws_sdk_neptunedata.errors import DeserializationError


class SparqlData(TypedDict):
    stmt: "str"
    r"""<p>Holds an <a href=\"https://www.w3.org/TR/n-quads/\">N-QUADS</a> statement expressing the changed quad.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SparqlData) -> dict:
    out: dict = {}
    out["stmt"] = value["stmt"]
    return out


def deserialize_json(data: dict) -> SparqlData:
    out: SparqlData = {}  # type: ignore[typeddict-item]
    if "stmt" in data:
        out["stmt"] = data["stmt"]
    else:
        raise DeserializationError("SparqlData.stmt required")
    return out
