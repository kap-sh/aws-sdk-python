"""Generated from Smithy shape ``com.amazonaws.sesv2#DeleteCustomVerificationEmailTemplateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.email_template_name


class DeleteCustomVerificationEmailTemplateRequest(TypedDict, closed=True):
    template_name: "aws_sdk_sesv2.types.email_template_name.EmailTemplateName"
    """<p>The name of the custom verification email template that you want to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteCustomVerificationEmailTemplateRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteCustomVerificationEmailTemplateRequest:
    out: DeleteCustomVerificationEmailTemplateRequest = {}  # type: ignore[typeddict-item]
    return out
