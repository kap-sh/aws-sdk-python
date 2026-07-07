"""Generated from Smithy shape ``com.amazonaws.qconnect#EmailMessageTemplateContent``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.email_headers
    import aws_sdk_qconnect.types.email_message_template_content_body
    import aws_sdk_qconnect.types.non_empty_unlimited_string


class EmailMessageTemplateContent(TypedDict, closed=True):
    subject: NotRequired[
        "aws_sdk_qconnect.types.non_empty_unlimited_string.NonEmptyUnlimitedString"
    ]
    """<p>The subject line, or title, to use in email messages.</p>"""
    body: NotRequired[
        "aws_sdk_qconnect.types.email_message_template_content_body.EmailMessageTemplateContentBody"
    ]
    """<p>The body to use in email messages.</p>"""
    headers: NotRequired["aws_sdk_qconnect.types.email_headers.EmailHeaders"]
    """<p>The email headers to include in email messages.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EmailMessageTemplateContent) -> dict:
    out: dict = {}
    if "subject" in value:
        out["subject"] = value["subject"]
    if "body" in value:
        import aws_sdk_qconnect.types.email_message_template_content_body

        out["body"] = (
            aws_sdk_qconnect.types.email_message_template_content_body.serialize_json(
                value["body"]
            )
        )
    if "headers" in value:
        import aws_sdk_qconnect.types.email_headers

        out["headers"] = aws_sdk_qconnect.types.email_headers.serialize_json(
            value["headers"]
        )
    return out


def deserialize_json(data: dict) -> EmailMessageTemplateContent:
    out: EmailMessageTemplateContent = {}  # type: ignore[typeddict-item]
    if "subject" in data:
        out["subject"] = data["subject"]
    if "body" in data:
        import aws_sdk_qconnect.types.email_message_template_content_body

        out["body"] = (
            aws_sdk_qconnect.types.email_message_template_content_body.deserialize_json(
                data["body"]
            )
        )
    if "headers" in data:
        import aws_sdk_qconnect.types.email_headers

        out["headers"] = aws_sdk_qconnect.types.email_headers.deserialize_json(
            data["headers"]
        )
    return out
