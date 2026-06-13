"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#ErrorBlock``."""

from typing import TypedDict

from typing_extensions import NotRequired


class ErrorBlock(TypedDict):
    message: NotRequired["str"]
    """<p>A human-readable error message describing what went wrong during content processing.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ErrorBlock) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ErrorBlock:
    out: ErrorBlock = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out
