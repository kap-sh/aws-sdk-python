"""Generated from Smithy shape ``com.amazonaws.connectparticipant#AttachmentItem``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connectparticipant.types.artifact_id
    import aws_sdk_connectparticipant.types.artifact_status
    import aws_sdk_connectparticipant.types.attachment_name
    import aws_sdk_connectparticipant.types.content_type


class AttachmentItem(TypedDict):
    content_type: NotRequired[
        "aws_sdk_connectparticipant.types.content_type.ContentType"
    ]
    """<p>Describes the MIME file type of the attachment. For a list of supported file types, see <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/feature-limits.html\">Feature specifications</a> in the <i>Amazon Connect Administrator Guide</i>.</p>"""
    attachment_id: NotRequired[
        "aws_sdk_connectparticipant.types.artifact_id.ArtifactId"
    ]
    """<p>A unique identifier for the attachment.</p>"""
    attachment_name: NotRequired[
        "aws_sdk_connectparticipant.types.attachment_name.AttachmentName"
    ]
    """<p>A case-sensitive name of the attachment being uploaded.</p>"""
    status: NotRequired[
        "aws_sdk_connectparticipant.types.artifact_status.ArtifactStatus"
    ]
    """<p>Status of the attachment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AttachmentItem) -> dict:
    out: dict = {}
    if "content_type" in value:
        out["ContentType"] = value["content_type"]
    if "attachment_id" in value:
        out["AttachmentId"] = value["attachment_id"]
    if "attachment_name" in value:
        out["AttachmentName"] = value["attachment_name"]
    if "status" in value:
        import aws_sdk_connectparticipant.types.artifact_status

        out["Status"] = aws_sdk_connectparticipant.types.artifact_status.serialize_json(
            value["status"]
        )
    return out


def deserialize_json(data: dict) -> AttachmentItem:
    out: AttachmentItem = {}  # type: ignore[typeddict-item]
    if "ContentType" in data:
        out["content_type"] = data["ContentType"]
    if "AttachmentId" in data:
        out["attachment_id"] = data["AttachmentId"]
    if "AttachmentName" in data:
        out["attachment_name"] = data["AttachmentName"]
    if "Status" in data:
        import aws_sdk_connectparticipant.types.artifact_status

        out["status"] = (
            aws_sdk_connectparticipant.types.artifact_status.deserialize_json(
                data["Status"]
            )
        )
    return out
