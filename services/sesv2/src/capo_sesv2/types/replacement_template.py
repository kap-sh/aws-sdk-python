"""Generated from Smithy shape ``com.amazonaws.sesv2#ReplacementTemplate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sesv2.types.email_template_data


class ReplacementTemplate(TypedDict, closed=True):
    replacement_template_data: NotRequired[
        "capo_sesv2.types.email_template_data.EmailTemplateData"
    ]
    """<p>A list of replacement values to apply to the template. This parameter is a JSON object, typically consisting of key-value pairs in which the keys correspond to replacement tags in the email template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReplacementTemplate) -> dict:
    out: dict = {}
    if "replacement_template_data" in value:
        out["ReplacementTemplateData"] = value["replacement_template_data"]
    return out


def deserialize_json(data: dict) -> ReplacementTemplate:
    out: ReplacementTemplate = {}  # type: ignore[typeddict-item]
    if "ReplacementTemplateData" in data:
        out["replacement_template_data"] = data["ReplacementTemplateData"]
    return out
