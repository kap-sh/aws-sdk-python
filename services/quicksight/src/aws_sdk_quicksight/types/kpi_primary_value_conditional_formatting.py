"""Generated from Smithy shape ``com.amazonaws.quicksight#KPIPrimaryValueConditionalFormatting``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.conditional_formatting_color
    import aws_sdk_quicksight.types.conditional_formatting_icon


class KPIPrimaryValueConditionalFormatting(TypedDict):
    text_color: NotRequired[
        "aws_sdk_quicksight.types.conditional_formatting_color.ConditionalFormattingColor"
    ]
    """<p>The conditional formatting of the primary value's text color.</p>"""
    icon: NotRequired[
        "aws_sdk_quicksight.types.conditional_formatting_icon.ConditionalFormattingIcon"
    ]
    """<p>The conditional formatting of the primary value's icon.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KPIPrimaryValueConditionalFormatting) -> dict:
    out: dict = {}
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


def deserialize_json(data: dict) -> KPIPrimaryValueConditionalFormatting:
    out: KPIPrimaryValueConditionalFormatting = {}  # type: ignore[typeddict-item]
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
