"""Generated from Smithy shape ``com.amazonaws.connect#ErrorResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.string


class ErrorResult(TypedDict):
    error_code: NotRequired["aws_sdk_connect.types.string.String"]
    """<p>The error code.</p>"""
    error_message: NotRequired["aws_sdk_connect.types.string.String"]
    """<p>The corresponding error message for the error code.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ErrorResult) -> dict:
    out: dict = {}
    if "error_code" in value:
        out["ErrorCode"] = value["error_code"]
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    return out


def deserialize_json(data: dict) -> ErrorResult:
    out: ErrorResult = {}  # type: ignore[typeddict-item]
    if "ErrorCode" in data:
        out["error_code"] = data["ErrorCode"]
    if "ErrorMessage" in data:
        out["error_message"] = data["ErrorMessage"]
    return out
