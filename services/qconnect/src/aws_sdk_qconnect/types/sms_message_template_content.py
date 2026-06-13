"""Generated from Smithy shape ``com.amazonaws.qconnect#SMSMessageTemplateContent``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.sms_message_template_content_body


class SMSMessageTemplateContent(TypedDict):
    body: NotRequired[
        "aws_sdk_qconnect.types.sms_message_template_content_body.SMSMessageTemplateContentBody"
    ]
    """<p>The body to use in SMS messages.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SMSMessageTemplateContent) -> dict:
    out: dict = {}
    if "body" in value:
        import aws_sdk_qconnect.types.sms_message_template_content_body

        out["body"] = (
            aws_sdk_qconnect.types.sms_message_template_content_body.serialize_json(
                value["body"]
            )
        )
    return out


def deserialize_json(data: dict) -> SMSMessageTemplateContent:
    out: SMSMessageTemplateContent = {}  # type: ignore[typeddict-item]
    if "body" in data:
        import aws_sdk_qconnect.types.sms_message_template_content_body

        out["body"] = (
            aws_sdk_qconnect.types.sms_message_template_content_body.deserialize_json(
                data["body"]
            )
        )
    return out
