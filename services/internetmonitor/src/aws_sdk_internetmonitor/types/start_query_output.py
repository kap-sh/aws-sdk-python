"""Generated from Smithy shape ``com.amazonaws.internetmonitor#StartQueryOutput``."""

from typing_extensions import TypedDict

from aws_sdk_internetmonitor.errors import DeserializationError


class StartQueryOutput(TypedDict, closed=True):
    query_id: "str"
    """<p>The internally-generated identifier of a specific query.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartQueryOutput) -> dict:
    out: dict = {}
    out["QueryId"] = value["query_id"]
    return out


def deserialize_json(data: dict) -> StartQueryOutput:
    out: StartQueryOutput = {}  # type: ignore[typeddict-item]
    if "QueryId" in data:
        out["query_id"] = data["QueryId"]
    else:
        raise DeserializationError("StartQueryOutput.query_id required")
    return out
