"""Generated from Smithy shape ``com.amazonaws.mwaa#UpdateError``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mwaa.types.error_code
    import capo_mwaa.types.error_message


class UpdateError(TypedDict, closed=True):
    error_code: NotRequired["capo_mwaa.types.error_code.ErrorCode"]
    """<p>The error code that corresponds to the error with the last update.</p>"""
    error_message: NotRequired["capo_mwaa.types.error_message.ErrorMessage"]
    """<p>The error message that corresponds to the error code.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateError) -> dict:
    out: dict = {}
    if "error_code" in value:
        out["ErrorCode"] = value["error_code"]
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    return out


def deserialize_json(data: dict) -> UpdateError:
    out: UpdateError = {}  # type: ignore[typeddict-item]
    if "ErrorCode" in data:
        out["error_code"] = data["ErrorCode"]
    if "ErrorMessage" in data:
        out["error_message"] = data["ErrorMessage"]
    return out
