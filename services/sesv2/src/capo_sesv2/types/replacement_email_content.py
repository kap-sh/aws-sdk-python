"""Generated from Smithy shape ``com.amazonaws.sesv2#ReplacementEmailContent``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sesv2.types.replacement_template


class ReplacementEmailContent(TypedDict, closed=True):
    replacement_template: NotRequired[
        "capo_sesv2.types.replacement_template.ReplacementTemplate"
    ]
    """<p>The <code>ReplacementTemplate</code> associated with <code>ReplacementEmailContent</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReplacementEmailContent) -> dict:
    out: dict = {}
    if "replacement_template" in value:
        import capo_sesv2.types.replacement_template

        out["ReplacementTemplate"] = (
            capo_sesv2.types.replacement_template.serialize_json(
                value["replacement_template"]
            )
        )
    return out


def deserialize_json(data: dict) -> ReplacementEmailContent:
    out: ReplacementEmailContent = {}  # type: ignore[typeddict-item]
    if "ReplacementTemplate" in data:
        import capo_sesv2.types.replacement_template

        out["replacement_template"] = (
            capo_sesv2.types.replacement_template.deserialize_json(
                data["ReplacementTemplate"]
            )
        )
    return out
