"""Generated from Smithy shape ``com.amazonaws.ses#CreateCustomVerificationEmailTemplateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_ses._protocol.xml import Element
from aws_sdk_ses.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ses.types.failure_redirection_url
    import aws_sdk_ses.types.from_address
    import aws_sdk_ses.types.subject
    import aws_sdk_ses.types.success_redirection_url
    import aws_sdk_ses.types.template_content
    import aws_sdk_ses.types.template_name


class CreateCustomVerificationEmailTemplateRequest(TypedDict, closed=True):
    template_name: "aws_sdk_ses.types.template_name.TemplateName"
    """<p>The name of the custom verification email template.</p>"""
    from_email_address: "aws_sdk_ses.types.from_address.FromAddress"
    """<p>The email address that the custom verification email is sent from.</p>"""
    template_subject: "aws_sdk_ses.types.subject.Subject"
    """<p>The subject line of the custom verification email.</p>"""
    template_content: "aws_sdk_ses.types.template_content.TemplateContent"
    r"""<p>The content of the custom verification email. The total size of the email must be less than 10 MB. The message body may contain HTML, with some limitations. For more information, see <a href=\"https://docs.aws.amazon.com/ses/latest/dg/creating-identities.html#send-email-verify-address-custom\">Custom Verification Email Frequently Asked Questions</a> in the <i>Amazon SES Developer Guide</i>.</p>"""
    success_redirection_url: (
        "aws_sdk_ses.types.success_redirection_url.SuccessRedirectionURL"
    )
    """<p>The URL that the recipient of the verification email is sent to if his or her address is successfully verified.</p>"""
    failure_redirection_url: (
        "aws_sdk_ses.types.failure_redirection_url.FailureRedirectionURL"
    )
    """<p>The URL that the recipient of the verification email is sent to if his or her address is not successfully verified.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateCustomVerificationEmailTemplateRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    pairs.append((f"{prefix}.TemplateName", str(value["template_name"])))
    pairs.append((f"{prefix}.FromEmailAddress", str(value["from_email_address"])))
    pairs.append((f"{prefix}.TemplateSubject", str(value["template_subject"])))
    pairs.append((f"{prefix}.TemplateContent", str(value["template_content"])))
    pairs.append(
        (f"{prefix}.SuccessRedirectionURL", str(value["success_redirection_url"]))
    )
    pairs.append(
        (f"{prefix}.FailureRedirectionURL", str(value["failure_redirection_url"]))
    )


def deserialize_query(el: Element) -> CreateCustomVerificationEmailTemplateRequest:
    out: CreateCustomVerificationEmailTemplateRequest = {}  # type: ignore[typeddict-item]
    child_template_name = el.find("TemplateName")
    if child_template_name is not None:
        out["template_name"] = str(child_template_name.text or "")
    else:
        raise DeserializationError(
            "CreateCustomVerificationEmailTemplateRequest.template_name required"
        )
    child_from_email_address = el.find("FromEmailAddress")
    if child_from_email_address is not None:
        out["from_email_address"] = str(child_from_email_address.text or "")
    else:
        raise DeserializationError(
            "CreateCustomVerificationEmailTemplateRequest.from_email_address required"
        )
    child_template_subject = el.find("TemplateSubject")
    if child_template_subject is not None:
        out["template_subject"] = str(child_template_subject.text or "")
    else:
        raise DeserializationError(
            "CreateCustomVerificationEmailTemplateRequest.template_subject required"
        )
    child_template_content = el.find("TemplateContent")
    if child_template_content is not None:
        out["template_content"] = str(child_template_content.text or "")
    else:
        raise DeserializationError(
            "CreateCustomVerificationEmailTemplateRequest.template_content required"
        )
    child_success_redirection_url = el.find("SuccessRedirectionURL")
    if child_success_redirection_url is not None:
        out["success_redirection_url"] = str(child_success_redirection_url.text or "")
    else:
        raise DeserializationError(
            "CreateCustomVerificationEmailTemplateRequest.success_redirection_url required"
        )
    child_failure_redirection_url = el.find("FailureRedirectionURL")
    if child_failure_redirection_url is not None:
        out["failure_redirection_url"] = str(child_failure_redirection_url.text or "")
    else:
        raise DeserializationError(
            "CreateCustomVerificationEmailTemplateRequest.failure_redirection_url required"
        )
    return out
