"""Generated from Smithy shape ``com.amazonaws.qbusiness#GetMediaResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qbusiness.types.blob
    import capo_qbusiness.types.string


class GetMediaResponse(TypedDict, closed=True):
    media_bytes: NotRequired["capo_qbusiness.types.blob.Blob"]
    """<p>The base64-encoded bytes of the media object.</p>"""
    media_mime_type: NotRequired["capo_qbusiness.types.string.String"]
    """<p>The MIME type of the media object (image/png).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMediaResponse) -> dict:
    out: dict = {}
    if "media_bytes" in value:
        import capo_qbusiness.types.blob

        out["mediaBytes"] = capo_qbusiness.types.blob.serialize_json(
            value["media_bytes"]
        )
    if "media_mime_type" in value:
        out["mediaMimeType"] = value["media_mime_type"]
    return out


def deserialize_json(data: dict) -> GetMediaResponse:
    out: GetMediaResponse = {}  # type: ignore[typeddict-item]
    if "mediaBytes" in data:
        import capo_qbusiness.types.blob

        out["media_bytes"] = capo_qbusiness.types.blob.deserialize_json(
            data["mediaBytes"]
        )
    if "mediaMimeType" in data:
        out["media_mime_type"] = data["mediaMimeType"]
    return out
