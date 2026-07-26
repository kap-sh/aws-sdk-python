"""Generated from Smithy shape ``com.amazonaws.quicksight#TextConditionalFormat``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.conditional_formatting_color
    import capo_quicksight.types.conditional_formatting_icon


class TextConditionalFormat(TypedDict, closed=True):
    background_color: NotRequired[
        "capo_quicksight.types.conditional_formatting_color.ConditionalFormattingColor"
    ]
    """<p>The conditional formatting for the text background color.</p>"""
    text_color: NotRequired[
        "capo_quicksight.types.conditional_formatting_color.ConditionalFormattingColor"
    ]
    """<p>The conditional formatting for the text color.</p>"""
    icon: NotRequired[
        "capo_quicksight.types.conditional_formatting_icon.ConditionalFormattingIcon"
    ]
    """<p>The conditional formatting for the icon.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TextConditionalFormat) -> dict:
    out: dict = {}
    if "background_color" in value:
        import capo_quicksight.types.conditional_formatting_color

        out["BackgroundColor"] = (
            capo_quicksight.types.conditional_formatting_color.serialize_json(
                value["background_color"]
            )
        )
    if "text_color" in value:
        import capo_quicksight.types.conditional_formatting_color

        out["TextColor"] = (
            capo_quicksight.types.conditional_formatting_color.serialize_json(
                value["text_color"]
            )
        )
    if "icon" in value:
        import capo_quicksight.types.conditional_formatting_icon

        out["Icon"] = capo_quicksight.types.conditional_formatting_icon.serialize_json(
            value["icon"]
        )
    return out


def deserialize_json(data: dict) -> TextConditionalFormat:
    out: TextConditionalFormat = {}  # type: ignore[typeddict-item]
    if "BackgroundColor" in data:
        import capo_quicksight.types.conditional_formatting_color

        out["background_color"] = (
            capo_quicksight.types.conditional_formatting_color.deserialize_json(
                data["BackgroundColor"]
            )
        )
    if "TextColor" in data:
        import capo_quicksight.types.conditional_formatting_color

        out["text_color"] = (
            capo_quicksight.types.conditional_formatting_color.deserialize_json(
                data["TextColor"]
            )
        )
    if "Icon" in data:
        import capo_quicksight.types.conditional_formatting_icon

        out["icon"] = (
            capo_quicksight.types.conditional_formatting_icon.deserialize_json(
                data["Icon"]
            )
        )
    return out
