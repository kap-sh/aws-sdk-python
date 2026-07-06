"""Generated from Smithy shape ``com.amazonaws.quicksight#GaugeChartPrimaryValueConditionalFormatting``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.conditional_formatting_color
    import aws_sdk_quicksight.types.conditional_formatting_icon


class GaugeChartPrimaryValueConditionalFormatting(TypedDict, closed=True):
    text_color: NotRequired[
        "aws_sdk_quicksight.types.conditional_formatting_color.ConditionalFormattingColor"
    ]
    """<p>The conditional formatting of the primary value text color.</p>"""
    icon: NotRequired[
        "aws_sdk_quicksight.types.conditional_formatting_icon.ConditionalFormattingIcon"
    ]
    """<p>The conditional formatting of the primary value icon.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GaugeChartPrimaryValueConditionalFormatting) -> dict:
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


def deserialize_json(data: dict) -> GaugeChartPrimaryValueConditionalFormatting:
    out: GaugeChartPrimaryValueConditionalFormatting = {}  # type: ignore[typeddict-item]
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
