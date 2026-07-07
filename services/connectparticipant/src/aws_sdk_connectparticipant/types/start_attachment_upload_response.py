"""Generated from Smithy shape ``com.amazonaws.connectparticipant#StartAttachmentUploadResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connectparticipant.types.artifact_id
    import aws_sdk_connectparticipant.types.upload_metadata


class StartAttachmentUploadResponse(TypedDict, closed=True):
    attachment_id: NotRequired[
        "aws_sdk_connectparticipant.types.artifact_id.ArtifactId"
    ]
    """<p>A unique identifier for the attachment.</p>"""
    upload_metadata: NotRequired[
        "aws_sdk_connectparticipant.types.upload_metadata.UploadMetadata"
    ]
    """<p>The headers to be provided while uploading the file to the URL.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartAttachmentUploadResponse) -> dict:
    out: dict = {}
    if "attachment_id" in value:
        out["AttachmentId"] = value["attachment_id"]
    if "upload_metadata" in value:
        import aws_sdk_connectparticipant.types.upload_metadata

        out["UploadMetadata"] = (
            aws_sdk_connectparticipant.types.upload_metadata.serialize_json(
                value["upload_metadata"]
            )
        )
    return out


def deserialize_json(data: dict) -> StartAttachmentUploadResponse:
    out: StartAttachmentUploadResponse = {}  # type: ignore[typeddict-item]
    if "AttachmentId" in data:
        out["attachment_id"] = data["AttachmentId"]
    if "UploadMetadata" in data:
        import aws_sdk_connectparticipant.types.upload_metadata

        out["upload_metadata"] = (
            aws_sdk_connectparticipant.types.upload_metadata.deserialize_json(
                data["UploadMetadata"]
            )
        )
    return out
