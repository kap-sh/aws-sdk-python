"""Generated from Smithy shape ``com.amazonaws.sesv2#GetEmailTemplateRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.email_template_name


class GetEmailTemplateRequest(TypedDict):
    template_name: "aws_sdk_sesv2.types.email_template_name.EmailTemplateName"
    """<p>The name of the template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetEmailTemplateRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetEmailTemplateRequest:
    out: GetEmailTemplateRequest = {}  # type: ignore[typeddict-item]
    return out
