"""Generated from Smithy shape ``com.amazonaws.sesv2#GetCustomVerificationEmailTemplateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_sesv2.types.email_template_name


class GetCustomVerificationEmailTemplateRequest(TypedDict, closed=True):
    template_name: "capo_sesv2.types.email_template_name.EmailTemplateName"
    """<p>The name of the custom verification email template that you want to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCustomVerificationEmailTemplateRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetCustomVerificationEmailTemplateRequest:
    out: GetCustomVerificationEmailTemplateRequest = {}  # type: ignore[typeddict-item]
    return out
