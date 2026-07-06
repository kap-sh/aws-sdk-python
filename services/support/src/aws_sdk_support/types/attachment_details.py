"""Generated from Smithy shape ``com.amazonaws.support#AttachmentDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_support.types.attachment_id
    import aws_sdk_support.types.file_name


class AttachmentDetails(TypedDict, closed=True):
    attachment_id: NotRequired["aws_sdk_support.types.attachment_id.AttachmentId"]
    """<p>The ID of the attachment.</p>"""
    file_name: NotRequired["aws_sdk_support.types.file_name.FileName"]
    """<p>The file name of the attachment.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AttachmentDetails) -> dict:
    out: dict = {}
    if "attachment_id" in value:
        out["attachmentId"] = value["attachment_id"]
    if "file_name" in value:
        out["fileName"] = value["file_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AttachmentDetails:
    out: AttachmentDetails = {}  # type: ignore[typeddict-item]
    if "attachmentId" in data:
        out["attachment_id"] = data["attachmentId"]
    if "fileName" in data:
        out["file_name"] = data["fileName"]
    return out
