"""Generated from Smithy shape ``com.amazonaws.mturk#GetFileUploadURLResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mturk.types.string


class GetFileUploadURLResponse(TypedDict, closed=True):
    file_upload_url: NotRequired["capo_mturk.types.string.String"]
    """<p> A temporary URL for the file that the Worker uploaded for the answer. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetFileUploadURLResponse) -> dict:
    out: dict = {}
    if "file_upload_url" in value:
        out["FileUploadURL"] = value["file_upload_url"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetFileUploadURLResponse:
    out: GetFileUploadURLResponse = {}  # type: ignore[typeddict-item]
    if "FileUploadURL" in data:
        out["file_upload_url"] = data["FileUploadURL"]
    return out
