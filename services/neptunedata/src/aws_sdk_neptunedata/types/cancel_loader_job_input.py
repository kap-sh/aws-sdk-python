"""Generated from Smithy shape ``com.amazonaws.neptunedata#CancelLoaderJobInput``."""

from typing import TypedDict

class CancelLoaderJobInput(TypedDict):
    load_id: "str"
    """<p>The ID of the load job to be deleted.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: CancelLoaderJobInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> CancelLoaderJobInput:
    out: CancelLoaderJobInput = {}  # type: ignore[typeddict-item]
    return out