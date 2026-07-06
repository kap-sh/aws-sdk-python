"""Generated from Smithy shape ``com.amazonaws.quicksight#GaugeChartConditionalFormatting``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.gauge_chart_conditional_formatting_option_list


class GaugeChartConditionalFormatting(TypedDict, closed=True):
    conditional_formatting_options: NotRequired[
        "aws_sdk_quicksight.types.gauge_chart_conditional_formatting_option_list.GaugeChartConditionalFormattingOptionList"
    ]
    """<p>Conditional formatting options of a <code>GaugeChartVisual</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GaugeChartConditionalFormatting) -> dict:
    out: dict = {}
    if "conditional_formatting_options" in value:
        import aws_sdk_quicksight.types.gauge_chart_conditional_formatting_option_list

        out["ConditionalFormattingOptions"] = (
            aws_sdk_quicksight.types.gauge_chart_conditional_formatting_option_list.serialize_json(
                value["conditional_formatting_options"]
            )
        )
    return out


def deserialize_json(data: dict) -> GaugeChartConditionalFormatting:
    out: GaugeChartConditionalFormatting = {}  # type: ignore[typeddict-item]
    if "ConditionalFormattingOptions" in data:
        import aws_sdk_quicksight.types.gauge_chart_conditional_formatting_option_list

        out["conditional_formatting_options"] = (
            aws_sdk_quicksight.types.gauge_chart_conditional_formatting_option_list.deserialize_json(
                data["ConditionalFormattingOptions"]
            )
        )
    return out
