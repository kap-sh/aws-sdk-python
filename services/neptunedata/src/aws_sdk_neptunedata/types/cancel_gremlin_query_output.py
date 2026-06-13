"""Generated from Smithy shape ``com.amazonaws.neptunedata#CancelGremlinQueryOutput``."""

from typing import TypedDict

from typing_extensions import NotRequired


class CancelGremlinQueryOutput(TypedDict):
    status: NotRequired["str"]
    """<p>The status of the cancelation</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CancelGremlinQueryOutput) -> dict:
    out: dict = {}
    if "status" in value:
        out["status"] = value["status"]
    return out


def deserialize_json(data: dict) -> CancelGremlinQueryOutput:
    out: CancelGremlinQueryOutput = {}  # type: ignore[typeddict-item]
    if "status" in data:
        out["status"] = data["status"]
    return out
