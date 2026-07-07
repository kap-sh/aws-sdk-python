"""Generated from Smithy shape ``com.amazonaws.qconnect#CreateMessageTemplateAttachmentResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.message_template_attachment


class CreateMessageTemplateAttachmentResponse(TypedDict, closed=True):
    attachment: NotRequired[
        "aws_sdk_qconnect.types.message_template_attachment.MessageTemplateAttachment"
    ]
    """<p>The message template attachment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateMessageTemplateAttachmentResponse) -> dict:
    out: dict = {}
    if "attachment" in value:
        import aws_sdk_qconnect.types.message_template_attachment

        out["attachment"] = (
            aws_sdk_qconnect.types.message_template_attachment.serialize_json(
                value["attachment"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateMessageTemplateAttachmentResponse:
    out: CreateMessageTemplateAttachmentResponse = {}  # type: ignore[typeddict-item]
    if "attachment" in data:
        import aws_sdk_qconnect.types.message_template_attachment

        out["attachment"] = (
            aws_sdk_qconnect.types.message_template_attachment.deserialize_json(
                data["attachment"]
            )
        )
    return out
