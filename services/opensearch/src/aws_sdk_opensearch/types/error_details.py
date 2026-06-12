"""Generated from Smithy shape ``com.amazonaws.opensearch#ErrorDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.error_message
    import aws_sdk_opensearch.types.error_type


class ErrorDetails(TypedDict):
    error_type: NotRequired["aws_sdk_opensearch.types.error_type.ErrorType"]
    """<p>The type of error that occurred.</p>"""
    error_message: NotRequired["aws_sdk_opensearch.types.error_message.ErrorMessage"]
    """<p>A message describing the error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ErrorDetails) -> dict:
    out: dict = {}
    if "error_type" in value:
        out["ErrorType"] = value["error_type"]
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    return out


def deserialize_json(data: dict) -> ErrorDetails:
    out: ErrorDetails = {}  # type: ignore[typeddict-item]
    if "ErrorType" in data:
        out["error_type"] = data["ErrorType"]
    if "ErrorMessage" in data:
        out["error_message"] = data["ErrorMessage"]
    return out
