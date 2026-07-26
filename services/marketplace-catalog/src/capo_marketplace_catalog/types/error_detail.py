"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#ErrorDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_catalog.types.error_code_string
    import capo_marketplace_catalog.types.exception_message_content


class ErrorDetail(TypedDict, closed=True):
    error_code: NotRequired[
        "capo_marketplace_catalog.types.error_code_string.ErrorCodeString"
    ]
    """<p>The error code that identifies the type of error.</p>"""
    error_message: NotRequired[
        "capo_marketplace_catalog.types.exception_message_content.ExceptionMessageContent"
    ]
    """<p>The message for the error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ErrorDetail) -> dict:
    out: dict = {}
    if "error_code" in value:
        out["ErrorCode"] = value["error_code"]
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    return out


def deserialize_json(data: dict) -> ErrorDetail:
    out: ErrorDetail = {}  # type: ignore[typeddict-item]
    if "ErrorCode" in data:
        out["error_code"] = data["ErrorCode"]
    if "ErrorMessage" in data:
        out["error_message"] = data["ErrorMessage"]
    return out
