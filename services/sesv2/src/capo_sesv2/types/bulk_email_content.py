"""Generated from Smithy shape ``com.amazonaws.sesv2#BulkEmailContent``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sesv2.types.template


class BulkEmailContent(TypedDict, closed=True):
    template: NotRequired["capo_sesv2.types.template.Template"]
    """<p>The template to use for the bulk email message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BulkEmailContent) -> dict:
    out: dict = {}
    if "template" in value:
        import capo_sesv2.types.template

        out["Template"] = capo_sesv2.types.template.serialize_json(value["template"])
    return out


def deserialize_json(data: dict) -> BulkEmailContent:
    out: BulkEmailContent = {}  # type: ignore[typeddict-item]
    if "Template" in data:
        import capo_sesv2.types.template

        out["template"] = capo_sesv2.types.template.deserialize_json(data["Template"])
    return out
