"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#ErrorBlock``."""

from typing_extensions import NotRequired, TypedDict


class ErrorBlock(TypedDict, closed=True):
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
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out
