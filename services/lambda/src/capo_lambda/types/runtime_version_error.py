"""Generated from Smithy shape ``com.amazonaws.lambda#RuntimeVersionError``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.sensitive_string
    import capo_lambda.types.string


class RuntimeVersionError(TypedDict, closed=True):
    error_code: NotRequired["capo_lambda.types.string.String"]
    """<p>The error code.</p>"""
    message: NotRequired["capo_lambda.types.sensitive_string.SensitiveString"]
    """<p>The error message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RuntimeVersionError) -> dict:
    out: dict = {}
    if "error_code" in value:
        out["ErrorCode"] = value["error_code"]
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> RuntimeVersionError:
    out: RuntimeVersionError = {}  # type: ignore[typeddict-item]
    if "ErrorCode" in data:
        out["error_code"] = data["ErrorCode"]
    if "Message" in data:
        out["message"] = data["Message"]
    return out
