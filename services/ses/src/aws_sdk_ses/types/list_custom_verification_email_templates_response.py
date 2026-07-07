"""Generated from Smithy shape ``com.amazonaws.ses#ListCustomVerificationEmailTemplatesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ses._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ses.types.custom_verification_email_templates
    import aws_sdk_ses.types.next_token


class ListCustomVerificationEmailTemplatesResponse(TypedDict, closed=True):
    custom_verification_email_templates: NotRequired[
        "aws_sdk_ses.types.custom_verification_email_templates.CustomVerificationEmailTemplates"
    ]
    """<p>A list of the custom verification email templates that exist in your account.</p>"""
    next_token: NotRequired["aws_sdk_ses.types.next_token.NextToken"]
    """<p>A token indicating that there are additional custom verification email templates available to be listed. Pass this token to a subsequent call to <code>ListTemplates</code> to retrieve the next 50 custom verification email templates.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ListCustomVerificationEmailTemplatesResponse,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "custom_verification_email_templates" in value:
        import aws_sdk_ses.types.custom_verification_email_templates

        aws_sdk_ses.types.custom_verification_email_templates.serialize_query(
            value["custom_verification_email_templates"],
            pairs,
            f"{prefix}.CustomVerificationEmailTemplates",
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_query(el: Element) -> ListCustomVerificationEmailTemplatesResponse:
    out: ListCustomVerificationEmailTemplatesResponse = {}  # type: ignore[typeddict-item]
    child_custom_verification_email_templates = el.find(
        "CustomVerificationEmailTemplates"
    )
    if child_custom_verification_email_templates is not None:
        import aws_sdk_ses.types.custom_verification_email_templates

        out["custom_verification_email_templates"] = (
            aws_sdk_ses.types.custom_verification_email_templates.deserialize_query(
                child_custom_verification_email_templates
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
