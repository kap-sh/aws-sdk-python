"""Generated from Smithy shape ``com.amazonaws.resourceexplorer2#ErrorDetails``."""

from typing_extensions import NotRequired, TypedDict


class ErrorDetails(TypedDict, closed=True):
    code: NotRequired["str"]
    """<p>The error code that identifies the type of error that occurred.</p>"""
    message: NotRequired["str"]
    """<p>A human-readable description of the error that occurred.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ErrorDetails) -> dict:
    out: dict = {}
    if "code" in value:
        out["Code"] = value["code"]
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ErrorDetails:
    out: ErrorDetails = {}  # type: ignore[typeddict-item]
    if "Code" in data:
        out["code"] = data["Code"]
    if "Message" in data:
        out["message"] = data["Message"]
    return out
