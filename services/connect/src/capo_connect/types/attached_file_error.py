"""Generated from Smithy shape ``com.amazonaws.connect#AttachedFileError``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.error_code
    import capo_connect.types.error_message
    import capo_connect.types.file_id


class AttachedFileError(TypedDict, closed=True):
    error_code: NotRequired["capo_connect.types.error_code.ErrorCode"]
    """<p> Status code describing the failure. </p>"""
    error_message: NotRequired["capo_connect.types.error_message.ErrorMessage"]
    """<p>Why the attached file couldn't be retrieved. </p>"""
    file_id: NotRequired["capo_connect.types.file_id.FileId"]
    """<p>The unique identifier of the attached file resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AttachedFileError) -> dict:
    out: dict = {}
    if "error_code" in value:
        out["ErrorCode"] = value["error_code"]
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    if "file_id" in value:
        out["FileId"] = value["file_id"]
    return out


def deserialize_json(data: dict) -> AttachedFileError:
    out: AttachedFileError = {}  # type: ignore[typeddict-item]
    if "ErrorCode" in data:
        out["error_code"] = data["ErrorCode"]
    if "ErrorMessage" in data:
        out["error_message"] = data["ErrorMessage"]
    if "FileId" in data:
        out["file_id"] = data["FileId"]
    return out
