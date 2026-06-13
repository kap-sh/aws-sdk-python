"""Generated from Smithy shape ``com.amazonaws.qconnect#SMSMessageTemplateContentBody``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.message_template_body_content_provider


class SMSMessageTemplateContentBody(TypedDict):
    plain_text: NotRequired[
        "aws_sdk_qconnect.types.message_template_body_content_provider.MessageTemplateBodyContentProvider"
    ]
    """<p>The message body to use in SMS messages.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SMSMessageTemplateContentBody) -> dict:
    out: dict = {}
    if "plain_text" in value:
        import aws_sdk_qconnect.types.message_template_body_content_provider

        out["plainText"] = (
            aws_sdk_qconnect.types.message_template_body_content_provider.serialize_json(
                value["plain_text"]
            )
        )
    return out


def deserialize_json(data: dict) -> SMSMessageTemplateContentBody:
    out: SMSMessageTemplateContentBody = {}  # type: ignore[typeddict-item]
    if "plainText" in data:
        import aws_sdk_qconnect.types.message_template_body_content_provider

        out["plain_text"] = (
            aws_sdk_qconnect.types.message_template_body_content_provider.deserialize_json(
                data["plainText"]
            )
        )
    return out
