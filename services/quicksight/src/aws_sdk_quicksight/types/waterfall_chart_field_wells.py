"""Generated from Smithy shape ``com.amazonaws.quicksight#WaterfallChartFieldWells``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.waterfall_chart_aggregated_field_wells


class WaterfallChartFieldWells(TypedDict):
    waterfall_chart_aggregated_field_wells: NotRequired[
        "aws_sdk_quicksight.types.waterfall_chart_aggregated_field_wells.WaterfallChartAggregatedFieldWells"
    ]
    """<p>The field well configuration of a waterfall visual.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WaterfallChartFieldWells) -> dict:
    out: dict = {}
    if "waterfall_chart_aggregated_field_wells" in value:
        import aws_sdk_quicksight.types.waterfall_chart_aggregated_field_wells

        out["WaterfallChartAggregatedFieldWells"] = (
            aws_sdk_quicksight.types.waterfall_chart_aggregated_field_wells.serialize_json(
                value["waterfall_chart_aggregated_field_wells"]
            )
        )
    return out


def deserialize_json(data: dict) -> WaterfallChartFieldWells:
    out: WaterfallChartFieldWells = {}  # type: ignore[typeddict-item]
    if "WaterfallChartAggregatedFieldWells" in data:
        import aws_sdk_quicksight.types.waterfall_chart_aggregated_field_wells

        out["waterfall_chart_aggregated_field_wells"] = (
            aws_sdk_quicksight.types.waterfall_chart_aggregated_field_wells.deserialize_json(
                data["WaterfallChartAggregatedFieldWells"]
            )
        )
    return out
