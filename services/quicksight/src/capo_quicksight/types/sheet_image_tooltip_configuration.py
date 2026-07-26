"""Generated from Smithy shape ``com.amazonaws.quicksight#SheetImageTooltipConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.sheet_image_tooltip_text
    import capo_quicksight.types.visibility


class SheetImageTooltipConfiguration(TypedDict, closed=True):
    tooltip_text: NotRequired[
        "capo_quicksight.types.sheet_image_tooltip_text.SheetImageTooltipText"
    ]
    """<p>The text that appears in the tooltip.</p>"""
    visibility: NotRequired["capo_quicksight.types.visibility.Visibility"]
    """<p>The visibility of the tooltip.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SheetImageTooltipConfiguration) -> dict:
    out: dict = {}
    if "tooltip_text" in value:
        import capo_quicksight.types.sheet_image_tooltip_text

        out["TooltipText"] = (
            capo_quicksight.types.sheet_image_tooltip_text.serialize_json(
                value["tooltip_text"]
            )
        )
    if "visibility" in value:
        import capo_quicksight.types.visibility

        out["Visibility"] = capo_quicksight.types.visibility.serialize_json(
            value["visibility"]
        )
    return out


def deserialize_json(data: dict) -> SheetImageTooltipConfiguration:
    out: SheetImageTooltipConfiguration = {}  # type: ignore[typeddict-item]
    if "TooltipText" in data:
        import capo_quicksight.types.sheet_image_tooltip_text

        out["tooltip_text"] = (
            capo_quicksight.types.sheet_image_tooltip_text.deserialize_json(
                data["TooltipText"]
            )
        )
    if "Visibility" in data:
        import capo_quicksight.types.visibility

        out["visibility"] = capo_quicksight.types.visibility.deserialize_json(
            data["Visibility"]
        )
    return out
