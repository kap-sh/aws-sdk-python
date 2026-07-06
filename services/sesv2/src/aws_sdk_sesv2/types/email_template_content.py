"""Generated from Smithy shape ``com.amazonaws.sesv2#EmailTemplateContent``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.email_template_html
    import aws_sdk_sesv2.types.email_template_subject
    import aws_sdk_sesv2.types.email_template_text


class EmailTemplateContent(TypedDict, closed=True):
    subject: NotRequired[
        "aws_sdk_sesv2.types.email_template_subject.EmailTemplateSubject"
    ]
    """<p>The subject line of the email.</p>"""
    text: NotRequired["aws_sdk_sesv2.types.email_template_text.EmailTemplateText"]
    """<p>The email body that will be visible to recipients whose email clients do not display HTML.</p>"""
    html: NotRequired["aws_sdk_sesv2.types.email_template_html.EmailTemplateHtml"]
    """<p>The HTML body of the email.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EmailTemplateContent) -> dict:
    out: dict = {}
    if "subject" in value:
        out["Subject"] = value["subject"]
    if "text" in value:
        out["Text"] = value["text"]
    if "html" in value:
        out["Html"] = value["html"]
    return out


def deserialize_json(data: dict) -> EmailTemplateContent:
    out: EmailTemplateContent = {}  # type: ignore[typeddict-item]
    if "Subject" in data:
        out["subject"] = data["Subject"]
    if "Text" in data:
        out["text"] = data["Text"]
    if "Html" in data:
        out["html"] = data["Html"]
    return out
