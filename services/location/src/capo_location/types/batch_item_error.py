"""Generated from Smithy shape ``com.amazonaws.location#BatchItemError``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_location.types.batch_item_error_code


class BatchItemError(TypedDict, closed=True):
    code: NotRequired["capo_location.types.batch_item_error_code.BatchItemErrorCode"]
    """<p>The error code associated with the batch request error.</p>"""
    message: NotRequired["str"]
    """<p>A message with the reason for the batch request error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchItemError) -> dict:
    out: dict = {}
    if "code" in value:
        out["Code"] = value["code"]
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> BatchItemError:
    out: BatchItemError = {}  # type: ignore[typeddict-item]
    if "Code" in data:
        out["code"] = data["Code"]
    if "Message" in data:
        out["message"] = data["Message"]
    return out
