"""Generated from Smithy shape ``com.amazonaws.sesv2#ListCustomVerificationEmailTemplatesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sesv2.types.custom_verification_email_templates_list
    import capo_sesv2.types.next_token


class ListCustomVerificationEmailTemplatesResponse(TypedDict, closed=True):
    custom_verification_email_templates: NotRequired[
        "capo_sesv2.types.custom_verification_email_templates_list.CustomVerificationEmailTemplatesList"
    ]
    """<p>A list of the custom verification email templates that exist in your account.</p>"""
    next_token: NotRequired["capo_sesv2.types.next_token.NextToken"]
    """<p>A token indicating that there are additional custom verification email templates available to be listed. Pass this token to a subsequent call to <code>ListCustomVerificationEmailTemplates</code> to retrieve the next 50 custom verification email templates.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCustomVerificationEmailTemplatesResponse) -> dict:
    out: dict = {}
    if "custom_verification_email_templates" in value:
        import capo_sesv2.types.custom_verification_email_templates_list

        out["CustomVerificationEmailTemplates"] = (
            capo_sesv2.types.custom_verification_email_templates_list.serialize_json(
                value["custom_verification_email_templates"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListCustomVerificationEmailTemplatesResponse:
    out: ListCustomVerificationEmailTemplatesResponse = {}  # type: ignore[typeddict-item]
    if "CustomVerificationEmailTemplates" in data:
        import capo_sesv2.types.custom_verification_email_templates_list

        out["custom_verification_email_templates"] = (
            capo_sesv2.types.custom_verification_email_templates_list.deserialize_json(
                data["CustomVerificationEmailTemplates"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
