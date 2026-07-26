"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#ErrorDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iottwinmaker.types.error_code
    import capo_iottwinmaker.types.error_message


class ErrorDetails(TypedDict, closed=True):
    code: NotRequired["capo_iottwinmaker.types.error_code.ErrorCode"]
    """<p>The error code.</p>"""
    message: NotRequired["capo_iottwinmaker.types.error_message.ErrorMessage"]
    """<p>The error message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ErrorDetails) -> dict:
    out: dict = {}
    if "code" in value:
        out["code"] = value["code"]
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ErrorDetails:
    out: ErrorDetails = {}  # type: ignore[typeddict-item]
    if "code" in data:
        out["code"] = data["code"]
    if "message" in data:
        out["message"] = data["message"]
    return out
