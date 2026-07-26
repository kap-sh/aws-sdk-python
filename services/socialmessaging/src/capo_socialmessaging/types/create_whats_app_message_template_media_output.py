"""Generated from Smithy shape ``com.amazonaws.socialmessaging#CreateWhatsAppMessageTemplateMediaOutput``."""

from typing_extensions import NotRequired, TypedDict


class CreateWhatsAppMessageTemplateMediaOutput(TypedDict, closed=True):
    meta_header_handle: NotRequired["str"]
    """<p>The handle assigned to the uploaded media by Meta, used to reference the media in templates.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateWhatsAppMessageTemplateMediaOutput) -> dict:
    out: dict = {}
    if "meta_header_handle" in value:
        out["metaHeaderHandle"] = value["meta_header_handle"]
    return out


def deserialize_json(data: dict) -> CreateWhatsAppMessageTemplateMediaOutput:
    out: CreateWhatsAppMessageTemplateMediaOutput = {}  # type: ignore[typeddict-item]
    if "metaHeaderHandle" in data:
        out["meta_header_handle"] = data["metaHeaderHandle"]
    return out
