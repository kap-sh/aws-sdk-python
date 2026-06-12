"""Generated from Smithy shape ``com.amazonaws.mturk#GetFileUploadURLResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mturk.types.string


class GetFileUploadURLResponse(TypedDict):
    file_upload_url: NotRequired["aws_sdk_mturk.types.string.String"]
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
