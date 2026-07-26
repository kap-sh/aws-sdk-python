"""Generated from Smithy shape ``com.amazonaws.quicksight#KbTemplateConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.kb_template


class KbTemplateConfiguration(TypedDict, closed=True):
    template: NotRequired["capo_quicksight.types.kb_template.KbTemplate"]
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
