"""Generated from Smithy shape ``com.amazonaws.quicksight#KbTemplateConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.kb_template


class KbTemplateConfiguration(TypedDict):
    template: NotRequired["aws_sdk_quicksight.types.kb_template.KbTemplate"]
    """<p>The template document that defines the knowledge base behavior.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KbTemplateConfiguration) -> dict:
    out: dict = {}
    if "template" in value:
        out["template"] = value["template"]
    return out


def deserialize_json(data: dict) -> KbTemplateConfiguration:
    out: KbTemplateConfiguration = {}  # type: ignore[typeddict-item]
    if "template" in data:
        out["template"] = data["template"]
    return out
