"""Generated from Smithy shape ``com.amazonaws.quicksight#GaugeChartConditionalFormattingOptionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.gauge_chart_conditional_formatting_option

GaugeChartConditionalFormattingOptionList: TypeAlias = list[
    "aws_sdk_quicksight.types.gauge_chart_conditional_formatting_option.GaugeChartConditionalFormattingOption"
]


# --- restJson1 ser/de ---
def serialize_json(value: GaugeChartConditionalFormattingOptionList) -> list:
    import aws_sdk_quicksight.types.gauge_chart_conditional_formatting_option

    out: list = []
    for item in value:
        out.append(
            aws_sdk_quicksight.types.gauge_chart_conditional_formatting_option.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> GaugeChartConditionalFormattingOptionList:
    import aws_sdk_quicksight.types.gauge_chart_conditional_formatting_option

    out: GaugeChartConditionalFormattingOptionList = []
    for item in data:
        out.append(
            aws_sdk_quicksight.types.gauge_chart_conditional_formatting_option.deserialize_json(
                item
            )
        )
    return out
