"""Generated from Smithy shape ``com.amazonaws.finspace#ErrorInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_finspace.types.error_details
    import capo_finspace.types.error_message


class ErrorInfo(TypedDict, closed=True):
    error_message: NotRequired["capo_finspace.types.error_message.ErrorMessage"]
    """<p>Specifies the error message that appears if a flow fails. </p>"""
    error_type: NotRequired["capo_finspace.types.error_details.ErrorDetails"]
    """<p>Specifies the type of error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ErrorInfo) -> dict:
    out: dict = {}
    if "error_message" in value:
        out["errorMessage"] = value["error_message"]
    if "error_type" in value:
        import capo_finspace.types.error_details

        out["errorType"] = capo_finspace.types.error_details.serialize_json(
            value["error_type"]
        )
    return out


def deserialize_json(data: dict) -> ErrorInfo:
    out: ErrorInfo = {}  # type: ignore[typeddict-item]
    if "errorMessage" in data:
        out["error_message"] = data["errorMessage"]
    if "errorType" in data:
        import capo_finspace.types.error_details

        out["error_type"] = capo_finspace.types.error_details.deserialize_json(
            data["errorType"]
        )
    return out
