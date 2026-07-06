"""Generated from Smithy shape ``com.amazonaws.quicksight#GaugeChartConditionalFormattingOption``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.gauge_chart_arc_conditional_formatting
    import aws_sdk_quicksight.types.gauge_chart_primary_value_conditional_formatting


class GaugeChartConditionalFormattingOption(TypedDict, closed=True):
    primary_value: NotRequired[
        "aws_sdk_quicksight.types.gauge_chart_primary_value_conditional_formatting.GaugeChartPrimaryValueConditionalFormatting"
    ]
    """<p>The conditional formatting for the primary value of a <code>GaugeChartVisual</code>.</p>"""
    arc: NotRequired[
        "aws_sdk_quicksight.types.gauge_chart_arc_conditional_formatting.GaugeChartArcConditionalFormatting"
    ]
    """<p>The options that determine the presentation of the arc of a <code>GaugeChartVisual</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GaugeChartConditionalFormattingOption) -> dict:
    out: dict = {}
    if "primary_value" in value:
        import aws_sdk_quicksight.types.gauge_chart_primary_value_conditional_formatting

        out["PrimaryValue"] = (
            aws_sdk_quicksight.types.gauge_chart_primary_value_conditional_formatting.serialize_json(
                value["primary_value"]
            )
        )
    if "arc" in value:
        import aws_sdk_quicksight.types.gauge_chart_arc_conditional_formatting

        out["Arc"] = (
            aws_sdk_quicksight.types.gauge_chart_arc_conditional_formatting.serialize_json(
                value["arc"]
            )
        )
    return out


def deserialize_json(data: dict) -> GaugeChartConditionalFormattingOption:
    out: GaugeChartConditionalFormattingOption = {}  # type: ignore[typeddict-item]
    if "PrimaryValue" in data:
        import aws_sdk_quicksight.types.gauge_chart_primary_value_conditional_formatting

        out["primary_value"] = (
            aws_sdk_quicksight.types.gauge_chart_primary_value_conditional_formatting.deserialize_json(
                data["PrimaryValue"]
            )
        )
    if "Arc" in data:
        import aws_sdk_quicksight.types.gauge_chart_arc_conditional_formatting

        out["arc"] = (
            aws_sdk_quicksight.types.gauge_chart_arc_conditional_formatting.deserialize_json(
                data["Arc"]
            )
        )
    return out
