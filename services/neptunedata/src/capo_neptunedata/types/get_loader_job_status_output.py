"""Generated from Smithy shape ``com.amazonaws.neptunedata#GetLoaderJobStatusOutput``."""

from typing_extensions import TypedDict

from capo_neptunedata.errors import DeserializationError


class GetLoaderJobStatusOutput(TypedDict, closed=True):
    status: "str"
    """<p>The HTTP response code for the request.</p>"""
    payload: "object"
    """<p>Status information about the load job, in a layout that could look like this:</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetLoaderJobStatusOutput) -> dict:
    out: dict = {}
    out["status"] = value["status"]
    out["payload"] = value["payload"]
    return out


def deserialize_json(data: dict) -> GetLoaderJobStatusOutput:
    out: GetLoaderJobStatusOutput = {}  # type: ignore[typeddict-item]
    if "status" in data:
        out["status"] = data["status"]
    else:
        raise DeserializationError("GetLoaderJobStatusOutput.status required")
    if "payload" in data:
        out["payload"] = data["payload"]
    else:
        raise DeserializationError("GetLoaderJobStatusOutput.payload required")
    return out
