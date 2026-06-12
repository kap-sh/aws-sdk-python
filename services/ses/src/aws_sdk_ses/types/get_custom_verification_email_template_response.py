"""Generated from Smithy shape ``com.amazonaws.ses#GetCustomVerificationEmailTemplateResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ses._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ses.types.failure_redirection_url
    import aws_sdk_ses.types.from_address
    import aws_sdk_ses.types.subject
    import aws_sdk_ses.types.success_redirection_url
    import aws_sdk_ses.types.template_content
    import aws_sdk_ses.types.template_name


class GetCustomVerificationEmailTemplateResponse(TypedDict):
    template_name: NotRequired["aws_sdk_ses.types.template_name.TemplateName"]
    """<p>The name of the custom verification email template.</p>"""
    from_email_address: NotRequired["aws_sdk_ses.types.from_address.FromAddress"]
    """<p>The email address that the custom verification email is sent from.</p>"""
    template_subject: NotRequired["aws_sdk_ses.types.subject.Subject"]
    """<p>The subject line of the custom verification email.</p>"""
    template_content: NotRequired["aws_sdk_ses.types.template_content.TemplateContent"]
    """<p>The content of the custom verification email.</p>"""
    success_redirection_url: NotRequired[
        "aws_sdk_ses.types.success_redirection_url.SuccessRedirectionURL"
    ]
    """<p>The URL that the recipient of the verification email is sent to if his or her address is successfully verified.</p>"""
    failure_redirection_url: NotRequired[
        "aws_sdk_ses.types.failure_redirection_url.FailureRedirectionURL"
    ]
    """<p>The URL that the recipient of the verification email is sent to if his or her address is not successfully verified.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: GetCustomVerificationEmailTemplateResponse,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "template_name" in value:
        pairs.append((f"{prefix}.TemplateName", str(value["template_name"])))
    if "from_email_address" in value:
        pairs.append((f"{prefix}.FromEmailAddress", str(value["from_email_address"])))
    if "template_subject" in value:
        pairs.append((f"{prefix}.TemplateSubject", str(value["template_subject"])))
    if "template_content" in value:
        pairs.append((f"{prefix}.TemplateContent", str(value["template_content"])))
    if "success_redirection_url" in value:
        pairs.append(
            (f"{prefix}.SuccessRedirectionURL", str(value["success_redirection_url"]))
        )
    if "failure_redirection_url" in value:
        pairs.append(
            (f"{prefix}.FailureRedirectionURL", str(value["failure_redirection_url"]))
        )


def deserialize_query(el: Element) -> GetCustomVerificationEmailTemplateResponse:
    out: GetCustomVerificationEmailTemplateResponse = {}  # type: ignore[typeddict-item]
    child_template_name = el.find("TemplateName")
    if child_template_name is not None:
        out["template_name"] = str(child_template_name.text or "")
    child_from_email_address = el.find("FromEmailAddress")
    if child_from_email_address is not None:
        out["from_email_address"] = str(child_from_email_address.text or "")
    child_template_subject = el.find("TemplateSubject")
    if child_template_subject is not None:
        out["template_subject"] = str(child_template_subject.text or "")
    child_template_content = el.find("TemplateContent")
    if child_template_content is not None:
        out["template_content"] = str(child_template_content.text or "")
    child_success_redirection_url = el.find("SuccessRedirectionURL")
    if child_success_redirection_url is not None:
        out["success_redirection_url"] = str(child_success_redirection_url.text or "")
    child_failure_redirection_url = el.find("FailureRedirectionURL")
    if child_failure_redirection_url is not None:
        out["failure_redirection_url"] = str(child_failure_redirection_url.text or "")
    return out
