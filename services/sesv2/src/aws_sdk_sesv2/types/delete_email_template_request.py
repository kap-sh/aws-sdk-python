"""Generated from Smithy shape ``com.amazonaws.sesv2#DeleteEmailTemplateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.email_template_name


class DeleteEmailTemplateRequest(TypedDict, closed=True):
    template_name: "aws_sdk_sesv2.types.email_template_name.EmailTemplateName"
    """<p>The name of the template to be deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteEmailTemplateRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteEmailTemplateRequest:
    out: DeleteEmailTemplateRequest = {}  # type: ignore[typeddict-item]
    return out
