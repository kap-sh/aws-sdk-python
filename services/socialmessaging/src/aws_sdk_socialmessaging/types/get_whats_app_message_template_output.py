"""Generated from Smithy shape ``com.amazonaws.socialmessaging#GetWhatsAppMessageTemplateOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_socialmessaging.types.meta_template


class GetWhatsAppMessageTemplateOutput(TypedDict, closed=True):
    template: NotRequired["aws_sdk_socialmessaging.types.meta_template.MetaTemplate"]
    """<p>The complete template definition as a JSON string (maximum 6000 characters).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetWhatsAppMessageTemplateOutput) -> dict:
    out: dict = {}
    if "template" in value:
        out["template"] = value["template"]
    return out


def deserialize_json(data: dict) -> GetWhatsAppMessageTemplateOutput:
    out: GetWhatsAppMessageTemplateOutput = {}  # type: ignore[typeddict-item]
    if "template" in data:
        out["template"] = data["template"]
    return out
