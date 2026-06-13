"""Generated from Smithy shape ``com.amazonaws.qconnect#WhatsAppMessageTemplateContent``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.whats_app_message_template_content_data


class WhatsAppMessageTemplateContent(TypedDict):
    data: NotRequired[
        "aws_sdk_qconnect.types.whats_app_message_template_content_data.WhatsAppMessageTemplateContentData"
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
