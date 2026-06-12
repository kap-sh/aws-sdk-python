"""Generated from Smithy shape ``com.amazonaws.sesv2#CustomVerificationEmailTemplateMetadata``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.email_address
    import aws_sdk_sesv2.types.email_template_name
    import aws_sdk_sesv2.types.email_template_subject
    import aws_sdk_sesv2.types.failure_redirection_url
    import aws_sdk_sesv2.types.success_redirection_url


class CustomVerificationEmailTemplateMetadata(TypedDict):
    template_name: NotRequired[
        "aws_sdk_sesv2.types.email_template_name.EmailTemplateName"
    ]
    """<p>The name of the custom verification email template.</p>"""
    from_email_address: NotRequired["aws_sdk_sesv2.types.email_address.EmailAddress"]
    """<p>The email address that the custom verification email is sent from.</p>"""
    template_subject: NotRequired[
        "aws_sdk_sesv2.types.email_template_subject.EmailTemplateSubject"
    ]
    """<p>The subject line of the custom verification email.</p>"""
    success_redirection_url: NotRequired[
        "aws_sdk_sesv2.types.success_redirection_url.SuccessRedirectionURL"
    ]
    """<p>The URL that the recipient of the verification email is sent to if his or her address is successfully verified.</p>"""
    failure_redirection_url: NotRequired[
        "aws_sdk_sesv2.types.failure_redirection_url.FailureRedirectionURL"
    ]
    """<p>The URL that the recipient of the verification email is sent to if his or her address is not successfully verified.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomVerificationEmailTemplateMetadata) -> dict:
    out: dict = {}
    if "template_name" in value:
        out["TemplateName"] = value["template_name"]
    if "from_email_address" in value:
        out["FromEmailAddress"] = value["from_email_address"]
    if "template_subject" in value:
        out["TemplateSubject"] = value["template_subject"]
    if "success_redirection_url" in value:
        out["SuccessRedirectionURL"] = value["success_redirection_url"]
    if "failure_redirection_url" in value:
        out["FailureRedirectionURL"] = value["failure_redirection_url"]
    return out


def deserialize_json(data: dict) -> CustomVerificationEmailTemplateMetadata:
    out: CustomVerificationEmailTemplateMetadata = {}  # type: ignore[typeddict-item]
    if "TemplateName" in data:
        out["template_name"] = data["TemplateName"]
    if "FromEmailAddress" in data:
        out["from_email_address"] = data["FromEmailAddress"]
    if "TemplateSubject" in data:
        out["template_subject"] = data["TemplateSubject"]
    if "SuccessRedirectionURL" in data:
        out["success_redirection_url"] = data["SuccessRedirectionURL"]
    if "FailureRedirectionURL" in data:
        out["failure_redirection_url"] = data["FailureRedirectionURL"]
    return out
