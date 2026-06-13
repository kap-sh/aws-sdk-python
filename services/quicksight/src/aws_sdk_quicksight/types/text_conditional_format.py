"""Generated from Smithy shape ``com.amazonaws.quicksight#TextConditionalFormat``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.conditional_formatting_color
    import aws_sdk_quicksight.types.conditional_formatting_icon


class TextConditionalFormat(TypedDict):
    background_color: NotRequired[
        "aws_sdk_quicksight.types.conditional_formatting_color.ConditionalFormattingColor"
    ]
    """<p>The conditional formatting for the text background color.</p>"""
    text_color: NotRequired[
        "aws_sdk_quicksight.types.conditional_formatting_color.ConditionalFormattingColor"
    ]
    """<p>The conditional formatting for the text color.</p>"""
    icon: NotRequired[
        "aws_sdk_quicksight.types.conditional_formatting_icon.ConditionalFormattingIcon"
    ]
    """<p>The conditional formatting for the icon.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TextConditionalFormat) -> dict:
    out: dict = {}
    if "background_color" in value:
        import aws_sdk_quicksight.types.conditional_formatting_color

        out["BackgroundColor"] = (
            aws_sdk_quicksight.types.conditional_formatting_color.serialize_json(
                value["background_color"]
            )
        )
    if "text_color" in value:
        import aws_sdk_quicksight.types.conditional_formatting_color

        out["TextColor"] = (
            aws_sdk_quicksight.types.conditional_formatting_color.serialize_json(
                value["text_color"]
            )
        )
    if "icon" in value:
        import aws_sdk_quicksight.types.conditional_formatting_icon

        out["Icon"] = (
            aws_sdk_quicksight.types.conditional_formatting_icon.serialize_json(
                value["icon"]
            )
        )
    return out


def deserialize_json(data: dict) -> TextConditionalFormat:
    out: TextConditionalFormat = {}  # type: ignore[typeddict-item]
    if "BackgroundColor" in data:
        import aws_sdk_quicksight.types.conditional_formatting_color

        out["background_color"] = (
            aws_sdk_quicksight.types.conditional_formatting_color.deserialize_json(
                data["BackgroundColor"]
            )
        )
    if "TextColor" in data:
        import aws_sdk_quicksight.types.conditional_formatting_color

        out["text_color"] = (
            aws_sdk_quicksight.types.conditional_formatting_color.deserialize_json(
                data["TextColor"]
            )
        )
    if "Icon" in data:
        import aws_sdk_quicksight.types.conditional_formatting_icon

        out["icon"] = (
            aws_sdk_quicksight.types.conditional_formatting_icon.deserialize_json(
                data["Icon"]
            )
        )
    return out
