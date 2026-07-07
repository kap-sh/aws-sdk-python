"""Generated from Smithy shape ``com.amazonaws.appstream#ErrorDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_appstream.types.string


class ErrorDetails(TypedDict, closed=True):
    error_code: NotRequired["aws_sdk_appstream.types.string.String"]
    """<p>The error code.</p>"""
    error_message: NotRequired["aws_sdk_appstream.types.string.String"]
    """<p>The error message.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ErrorDetails) -> dict:
    out: dict = {}
    if "error_code" in value:
        out["ErrorCode"] = value["error_code"]
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ErrorDetails:
    out: ErrorDetails = {}  # type: ignore[typeddict-item]
    if "ErrorCode" in data:
        out["error_code"] = data["ErrorCode"]
    if "ErrorMessage" in data:
        out["error_message"] = data["ErrorMessage"]
    return out
