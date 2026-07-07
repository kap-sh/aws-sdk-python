"""Generated from Smithy shape ``com.amazonaws.quicksight#TableRowConditionalFormatting``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.conditional_formatting_color


class TableRowConditionalFormatting(TypedDict, closed=True):
    background_color: NotRequired[
        "aws_sdk_quicksight.types.conditional_formatting_color.ConditionalFormattingColor"
    ]
    """<p>The conditional formatting color (solid, gradient) of the background for a table row.</p>"""
    text_color: NotRequired[
        "aws_sdk_quicksight.types.conditional_formatting_color.ConditionalFormattingColor"
    ]
    """<p>The conditional formatting color (solid, gradient) of the text for a table row.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TableRowConditionalFormatting) -> dict:
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
    return out


def deserialize_json(data: dict) -> TableRowConditionalFormatting:
    out: TableRowConditionalFormatting = {}  # type: ignore[typeddict-item]
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
    return out
