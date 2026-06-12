"""Generated from Smithy shape ``com.amazonaws.socialmessaging#DeleteWhatsAppMessageMediaOutput``."""

from typing import TypedDict

from typing_extensions import NotRequired


class DeleteWhatsAppMessageMediaOutput(TypedDict):
    success: NotRequired["bool"]
    """<p>Success indicator for deleting the media file.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteWhatsAppMessageMediaOutput) -> dict:
    out: dict = {}
    if "success" in value:
        out["success"] = value["success"]
    return out


def deserialize_json(data: dict) -> DeleteWhatsAppMessageMediaOutput:
    out: DeleteWhatsAppMessageMediaOutput = {}  # type: ignore[typeddict-item]
    if "success" in data:
        out["success"] = data["success"]
    return out
