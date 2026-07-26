"""Generated from Smithy shape ``com.amazonaws.sesv2#GetCustomVerificationEmailTemplateResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sesv2.types.email_address
    import capo_sesv2.types.email_template_name
    import capo_sesv2.types.email_template_subject
    import capo_sesv2.types.failure_redirection_url
    import capo_sesv2.types.success_redirection_url
    import capo_sesv2.types.tag_list
    import capo_sesv2.types.template_content


class GetCustomVerificationEmailTemplateResponse(TypedDict, closed=True):
    template_name: NotRequired["capo_sesv2.types.email_template_name.EmailTemplateName"]
    """<p>The name of the custom verification email template.</p>"""
    from_email_address: NotRequired["capo_sesv2.types.email_address.EmailAddress"]
    """<p>The email address that the custom verification email is sent from.</p>"""
    template_subject: NotRequired[
        "capo_sesv2.types.email_template_subject.EmailTemplateSubject"
    ]
    """<p>The subject line of the custom verification email.</p>"""
    template_content: NotRequired["capo_sesv2.types.template_content.TemplateContent"]
    """<p>The content of the custom verification email.</p>"""
    tags: NotRequired["capo_sesv2.types.tag_list.TagList"]
    """<p>An array of objects that define the tags (keys and values) that are associated with the custom verification email template.</p>"""
    success_redirection_url: NotRequired[
        "capo_sesv2.types.success_redirection_url.SuccessRedirectionURL"
    ]
    """<p>The URL that the recipient of the verification email is sent to if his or her address is successfully verified.</p>"""
    failure_redirection_url: NotRequired[
        "capo_sesv2.types.failure_redirection_url.FailureRedirectionURL"
    ]
    """<p>The URL that the recipient of the verification email is sent to if his or her address is not successfully verified.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCustomVerificationEmailTemplateResponse) -> dict:
    out: dict = {}
    if "template_name" in value:
        out["TemplateName"] = value["template_name"]
    if "from_email_address" in value:
        out["FromEmailAddress"] = value["from_email_address"]
    if "template_subject" in value:
        out["TemplateSubject"] = value["template_subject"]
    if "template_content" in value:
        out["TemplateContent"] = value["template_content"]
    if "tags" in value:
        import capo_sesv2.types.tag_list

        out["Tags"] = capo_sesv2.types.tag_list.serialize_json(value["tags"])
    if "success_redirection_url" in value:
        out["SuccessRedirectionURL"] = value["success_redirection_url"]
    if "failure_redirection_url" in value:
        out["FailureRedirectionURL"] = value["failure_redirection_url"]
    return out


def deserialize_json(data: dict) -> GetCustomVerificationEmailTemplateResponse:
    out: GetCustomVerificationEmailTemplateResponse = {}  # type: ignore[typeddict-item]
    if "TemplateName" in data:
        out["template_name"] = data["TemplateName"]
    if "FromEmailAddress" in data:
        out["from_email_address"] = data["FromEmailAddress"]
    if "TemplateSubject" in data:
        out["template_subject"] = data["TemplateSubject"]
    if "TemplateContent" in data:
        out["template_content"] = data["TemplateContent"]
    if "Tags" in data:
        import capo_sesv2.types.tag_list

        out["tags"] = capo_sesv2.types.tag_list.deserialize_json(data["Tags"])
    if "SuccessRedirectionURL" in data:
        out["success_redirection_url"] = data["SuccessRedirectionURL"]
    if "FailureRedirectionURL" in data:
        out["failure_redirection_url"] = data["FailureRedirectionURL"]
    return out
