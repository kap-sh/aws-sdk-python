"""Generated from Smithy shape ``com.amazonaws.quicksight#GaugeChartArcConditionalFormatting``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.conditional_formatting_color


class GaugeChartArcConditionalFormatting(TypedDict):
    foreground_color: NotRequired[
        "aws_sdk_quicksight.types.conditional_formatting_color.ConditionalFormattingColor"
    ]
    """<p>The conditional formatting of the arc foreground color.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GaugeChartArcConditionalFormatting) -> dict:
    out: dict = {}
    if "foreground_color" in value:
        import aws_sdk_quicksight.types.conditional_formatting_color

        out["ForegroundColor"] = (
            aws_sdk_quicksight.types.conditional_formatting_color.serialize_json(
                value["foreground_color"]
            )
        )
    return out


def deserialize_json(data: dict) -> GaugeChartArcConditionalFormatting:
    out: GaugeChartArcConditionalFormatting = {}  # type: ignore[typeddict-item]
    if "ForegroundColor" in data:
        import aws_sdk_quicksight.types.conditional_formatting_color

        out["foreground_color"] = (
            aws_sdk_quicksight.types.conditional_formatting_color.deserialize_json(
                data["ForegroundColor"]
            )
        )
    return out
