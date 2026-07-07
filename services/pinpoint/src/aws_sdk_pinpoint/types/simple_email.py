"""Generated from Smithy shape ``com.amazonaws.pinpoint#SimpleEmail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.list_of_message_header
    import aws_sdk_pinpoint.types.simple_email_part


class SimpleEmail(TypedDict, closed=True):
    html_part: NotRequired["aws_sdk_pinpoint.types.simple_email_part.SimpleEmailPart"]
    """<p>The body of the email message, in HTML format. We recommend using HTML format for email clients that render HTML content. You can include links, formatted text, and more in an HTML message.</p>"""
    subject: NotRequired["aws_sdk_pinpoint.types.simple_email_part.SimpleEmailPart"]
    """<p>The subject line, or title, of the email.</p>"""
    text_part: NotRequired["aws_sdk_pinpoint.types.simple_email_part.SimpleEmailPart"]
    """<p>The body of the email message, in plain text format. We recommend using plain text format for email clients that don't render HTML content and clients that are connected to high-latency networks, such as mobile devices.</p>"""
    headers: NotRequired[
        "aws_sdk_pinpoint.types.list_of_message_header.ListOfMessageHeader"
    ]
    """<p>The list of MessageHeaders for the email. You can have up to 15 Headers.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SimpleEmail) -> dict:
    out: dict = {}
    if "html_part" in value:
        import aws_sdk_pinpoint.types.simple_email_part

        out["HtmlPart"] = aws_sdk_pinpoint.types.simple_email_part.serialize_json(
            value["html_part"]
        )
    if "subject" in value:
        import aws_sdk_pinpoint.types.simple_email_part

        out["Subject"] = aws_sdk_pinpoint.types.simple_email_part.serialize_json(
            value["subject"]
        )
    if "text_part" in value:
        import aws_sdk_pinpoint.types.simple_email_part

        out["TextPart"] = aws_sdk_pinpoint.types.simple_email_part.serialize_json(
            value["text_part"]
        )
    if "headers" in value:
        import aws_sdk_pinpoint.types.list_of_message_header

        out["Headers"] = aws_sdk_pinpoint.types.list_of_message_header.serialize_json(
            value["headers"]
        )
    return out


def deserialize_json(data: dict) -> SimpleEmail:
    out: SimpleEmail = {}  # type: ignore[typeddict-item]
    if "HtmlPart" in data:
        import aws_sdk_pinpoint.types.simple_email_part

        out["html_part"] = aws_sdk_pinpoint.types.simple_email_part.deserialize_json(
            data["HtmlPart"]
        )
    if "Subject" in data:
        import aws_sdk_pinpoint.types.simple_email_part

        out["subject"] = aws_sdk_pinpoint.types.simple_email_part.deserialize_json(
            data["Subject"]
        )
    if "TextPart" in data:
        import aws_sdk_pinpoint.types.simple_email_part

        out["text_part"] = aws_sdk_pinpoint.types.simple_email_part.deserialize_json(
            data["TextPart"]
        )
    if "Headers" in data:
        import aws_sdk_pinpoint.types.list_of_message_header

        out["headers"] = aws_sdk_pinpoint.types.list_of_message_header.deserialize_json(
            data["Headers"]
        )
    return out
