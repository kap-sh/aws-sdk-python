"""Generated from Smithy shape ``com.amazonaws.s3outposts#FailedReason``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_s3outposts.types.error_code
    import capo_s3outposts.types.message


class FailedReason(TypedDict, closed=True):
    error_code: NotRequired["capo_s3outposts.types.error_code.ErrorCode"]
    """<p>The failure code, if any, for a create or delete endpoint operation.</p>"""
    message: NotRequired["capo_s3outposts.types.message.Message"]
    """<p>Additional error details describing the endpoint failure and recommended action.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FailedReason) -> dict:
    out: dict = {}
    if "error_code" in value:
        out["ErrorCode"] = value["error_code"]
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> FailedReason:
    out: FailedReason = {}  # type: ignore[typeddict-item]
    if "ErrorCode" in data:
        out["error_code"] = data["ErrorCode"]
    if "Message" in data:
        out["message"] = data["Message"]
    return out
