"""Generated from Smithy shape ``com.amazonaws.quicksight#SnapshotJobErrorInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.string


class SnapshotJobErrorInfo(TypedDict, closed=True):
    error_message: NotRequired["capo_quicksight.types.string.String"]
    """<p>The error message.</p>"""
    error_type: NotRequired["capo_quicksight.types.string.String"]
    """<p>The error type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SnapshotJobErrorInfo) -> dict:
    out: dict = {}
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    if "error_type" in value:
        out["ErrorType"] = value["error_type"]
    return out


def deserialize_json(data: dict) -> SnapshotJobErrorInfo:
    out: SnapshotJobErrorInfo = {}  # type: ignore[typeddict-item]
    if "ErrorMessage" in data:
        out["error_message"] = data["ErrorMessage"]
    if "ErrorType" in data:
        out["error_type"] = data["ErrorType"]
    return out
