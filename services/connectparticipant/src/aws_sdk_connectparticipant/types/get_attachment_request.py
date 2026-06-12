"""Generated from Smithy shape ``com.amazonaws.connectparticipant#GetAttachmentRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_connectparticipant.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connectparticipant.types.artifact_id
    import aws_sdk_connectparticipant.types.participant_token
    import aws_sdk_connectparticipant.types.url_expiry_in_seconds


class GetAttachmentRequest(TypedDict):
    attachment_id: "aws_sdk_connectparticipant.types.artifact_id.ArtifactId"
    """<p>A unique identifier for the attachment.</p>"""
    connection_token: (
        "aws_sdk_connectparticipant.types.participant_token.ParticipantToken"
    )
    """<p>The authentication token associated with the participant's connection.</p>"""
    url_expiry_in_seconds: NotRequired[
        "aws_sdk_connectparticipant.types.url_expiry_in_seconds.URLExpiryInSeconds"
    ]
    """<p>The expiration time of the URL in ISO timestamp. It's specified in ISO 8601 format: yyyy-MM-ddThh:mm:ss.SSSZ. For example, 2019-11-08T02:41:28.172Z.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAttachmentRequest) -> dict:
    out: dict = {}
    out["AttachmentId"] = value["attachment_id"]
    if "url_expiry_in_seconds" in value:
        out["UrlExpiryInSeconds"] = value["url_expiry_in_seconds"]
    return out


def deserialize_json(data: dict) -> GetAttachmentRequest:
    out: GetAttachmentRequest = {}  # type: ignore[typeddict-item]
    if "AttachmentId" in data:
        out["attachment_id"] = data["AttachmentId"]
    else:
        raise DeserializationError("GetAttachmentRequest.attachment_id required")
    if "UrlExpiryInSeconds" in data:
        out["url_expiry_in_seconds"] = data["UrlExpiryInSeconds"]
    return out
