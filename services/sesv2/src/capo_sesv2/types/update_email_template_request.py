"""Generated from Smithy shape ``com.amazonaws.sesv2#UpdateEmailTemplateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_sesv2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_sesv2.types.email_template_content
    import capo_sesv2.types.email_template_name


class UpdateEmailTemplateRequest(TypedDict, closed=True):
    template_name: "capo_sesv2.types.email_template_name.EmailTemplateName"
    """<p>The name of the template.</p>"""
    template_content: "capo_sesv2.types.email_template_content.EmailTemplateContent"
    """<p>The content of the email template, composed of a subject line, an HTML part, and a text-only part.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateEmailTemplateRequest) -> dict:
    out: dict = {}
    import capo_sesv2.types.email_template_content

    out["TemplateContent"] = capo_sesv2.types.email_template_content.serialize_json(
        value["template_content"]
    )
    return out


def deserialize_json(data: dict) -> UpdateEmailTemplateRequest:
    out: UpdateEmailTemplateRequest = {}  # type: ignore[typeddict-item]
    if "TemplateContent" in data:
        import capo_sesv2.types.email_template_content

        out["template_content"] = (
            capo_sesv2.types.email_template_content.deserialize_json(
                data["TemplateContent"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateEmailTemplateRequest.template_content required"
        )
    return out
