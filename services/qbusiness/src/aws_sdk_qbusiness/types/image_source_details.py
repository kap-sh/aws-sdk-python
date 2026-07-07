"""Generated from Smithy shape ``com.amazonaws.qbusiness#ImageSourceDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.media_id
    import aws_sdk_qbusiness.types.string


class ImageSourceDetails(TypedDict, closed=True):
    media_id: NotRequired["aws_sdk_qbusiness.types.media_id.MediaId"]
    """<p>Unique identifier for the image file.</p>"""
    media_mime_type: NotRequired["aws_sdk_qbusiness.types.string.String"]
    """<p>The MIME type of the image file.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImageSourceDetails) -> dict:
    out: dict = {}
    if "media_id" in value:
        out["mediaId"] = value["media_id"]
    if "media_mime_type" in value:
        out["mediaMimeType"] = value["media_mime_type"]
    return out


def deserialize_json(data: dict) -> ImageSourceDetails:
    out: ImageSourceDetails = {}  # type: ignore[typeddict-item]
    if "mediaId" in data:
        out["media_id"] = data["mediaId"]
    if "mediaMimeType" in data:
        out["media_mime_type"] = data["mediaMimeType"]
    return out
