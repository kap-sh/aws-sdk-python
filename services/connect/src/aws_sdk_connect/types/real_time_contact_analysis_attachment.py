"""Generated from Smithy shape ``com.amazonaws.connect#RealTimeContactAnalysisAttachment``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.artifact_id
    import aws_sdk_connect.types.artifact_status
    import aws_sdk_connect.types.attachment_name
    import aws_sdk_connect.types.content_type


class RealTimeContactAnalysisAttachment(TypedDict):
    attachment_name: "aws_sdk_connect.types.attachment_name.AttachmentName"
    """<p>A case-sensitive name of the attachment being uploaded. Can be redacted.</p>"""
    content_type: NotRequired["aws_sdk_connect.types.content_type.ContentType"]
    """<p>Describes the MIME file type of the attachment. For a list of supported file types, see <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/feature-limits.html\">Feature specifications</a> in the <i>Connect Customer Administrator Guide</i>.</p>"""
    attachment_id: "aws_sdk_connect.types.artifact_id.ArtifactId"
    """<p>A unique identifier for the attachment.</p>"""
    status: NotRequired["aws_sdk_connect.types.artifact_status.ArtifactStatus"]
    """<p>Status of the attachment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RealTimeContactAnalysisAttachment) -> dict:
    out: dict = {}
    out["AttachmentName"] = value["attachment_name"]
    if "content_type" in value:
        out["ContentType"] = value["content_type"]
    out["AttachmentId"] = value["attachment_id"]
    if "status" in value:
        import aws_sdk_connect.types.artifact_status

        out["Status"] = aws_sdk_connect.types.artifact_status.serialize_json(
            value["status"]
        )
    return out


def deserialize_json(data: dict) -> RealTimeContactAnalysisAttachment:
    out: RealTimeContactAnalysisAttachment = {}  # type: ignore[typeddict-item]
    if "AttachmentName" in data:
        out["attachment_name"] = data["AttachmentName"]
    else:
        raise DeserializationError(
            "RealTimeContactAnalysisAttachment.attachment_name required"
        )
    if "ContentType" in data:
        out["content_type"] = data["ContentType"]
    if "AttachmentId" in data:
        out["attachment_id"] = data["AttachmentId"]
    else:
        raise DeserializationError(
            "RealTimeContactAnalysisAttachment.attachment_id required"
        )
    if "Status" in data:
        import aws_sdk_connect.types.artifact_status

        out["status"] = aws_sdk_connect.types.artifact_status.deserialize_json(
            data["Status"]
        )
    return out
