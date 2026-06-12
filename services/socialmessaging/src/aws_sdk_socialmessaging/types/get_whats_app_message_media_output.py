"""Generated from Smithy shape ``com.amazonaws.socialmessaging#GetWhatsAppMessageMediaOutput``."""

from typing import TypedDict

from typing_extensions import NotRequired


class GetWhatsAppMessageMediaOutput(TypedDict):
    mime_type: NotRequired["str"]
    """<p>The MIME type of the media.</p>"""
    file_size: NotRequired["int"]
    """<p>The size of the media file, in KB.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetWhatsAppMessageMediaOutput) -> dict:
    out: dict = {}
    if "mime_type" in value:
        out["mimeType"] = value["mime_type"]
    if "file_size" in value:
        out["fileSize"] = value["file_size"]
    return out


def deserialize_json(data: dict) -> GetWhatsAppMessageMediaOutput:
    out: GetWhatsAppMessageMediaOutput = {}  # type: ignore[typeddict-item]
    if "mimeType" in data:
        out["mime_type"] = data["mimeType"]
    if "fileSize" in data:
        out["file_size"] = data["fileSize"]
    return out
