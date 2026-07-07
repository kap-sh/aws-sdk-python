"""Generated from Smithy shape ``com.amazonaws.lambda#EnvironmentError``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lambda.types.sensitive_string
    import aws_sdk_lambda.types.string


class EnvironmentError(TypedDict, closed=True):
    error_code: NotRequired["aws_sdk_lambda.types.string.String"]
    """<p>The error code.</p>"""
    message: NotRequired["aws_sdk_lambda.types.sensitive_string.SensitiveString"]
    """<p>The error message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EnvironmentError) -> dict:
    out: dict = {}
    if "error_code" in value:
        out["ErrorCode"] = value["error_code"]
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> EnvironmentError:
    out: EnvironmentError = {}  # type: ignore[typeddict-item]
    if "ErrorCode" in data:
        out["error_code"] = data["ErrorCode"]
    if "Message" in data:
        out["message"] = data["Message"]
    return out
