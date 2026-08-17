"""Generated from Smithy shape ``com.amazonaws.lambda#ImageConfigError``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.sensitive_string
    import capo_lambda.types.string


class ImageConfigError(TypedDict, closed=True):
    error_code: NotRequired["capo_lambda.types.string.String"]
    """<p>Error code.</p>"""
    message: NotRequired["capo_lambda.types.sensitive_string.SensitiveString"]
    """<p>Error message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImageConfigError) -> dict:
    out: dict = {}
    if "error_code" in value:
        out["ErrorCode"] = value["error_code"]
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ImageConfigError:
    out: ImageConfigError = {}  # type: ignore[typeddict-item]
    if data.get("ErrorCode") is not None:
        out["error_code"] = data["ErrorCode"]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out
