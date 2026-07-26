"""Generated from Smithy shape ``com.amazonaws.qconnect#WhatsAppMessageTemplateContent``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qconnect.types.whats_app_message_template_content_data


class WhatsAppMessageTemplateContent(TypedDict, closed=True):
    data: NotRequired[
        "capo_qconnect.types.whats_app_message_template_content_data.WhatsAppMessageTemplateContentData"
    ]
    """<p>The data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WhatsAppMessageTemplateContent) -> dict:
    out: dict = {}
    if "data" in value:
        out["data"] = value["data"]
    return out


def deserialize_json(data: dict) -> WhatsAppMessageTemplateContent:
    out: WhatsAppMessageTemplateContent = {}  # type: ignore[typeddict-item]
    if "data" in data:
        out["data"] = data["data"]
    return out
