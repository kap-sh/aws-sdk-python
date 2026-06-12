"""Generated from Smithy shape ``com.amazonaws.neptunedata#CancelLoaderJobOutput``."""

from typing import TypedDict
from typing_extensions import NotRequired

class CancelLoaderJobOutput(TypedDict):
    status: NotRequired["str"]
    """<p>The cancellation status.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: CancelLoaderJobOutput) -> dict:
    out: dict = {}
    if "status" in value:
        out["status"] = value["status"]
    return out


def deserialize_json(data: dict) -> CancelLoaderJobOutput:
    out: CancelLoaderJobOutput = {}  # type: ignore[typeddict-item]
    if "status" in data:
        out["status"] = data["status"]
    return out