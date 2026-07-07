"""Generated from Smithy shape ``com.amazonaws.quicksight#PieChartFieldWells``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.pie_chart_aggregated_field_wells


class PieChartFieldWells(TypedDict, closed=True):
    pie_chart_aggregated_field_wells: NotRequired[
        "aws_sdk_quicksight.types.pie_chart_aggregated_field_wells.PieChartAggregatedFieldWells"
    ]
    """<p>The field well configuration of a pie chart.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PieChartFieldWells) -> dict:
    out: dict = {}
    if "pie_chart_aggregated_field_wells" in value:
        import aws_sdk_quicksight.types.pie_chart_aggregated_field_wells

        out["PieChartAggregatedFieldWells"] = (
            aws_sdk_quicksight.types.pie_chart_aggregated_field_wells.serialize_json(
                value["pie_chart_aggregated_field_wells"]
            )
        )
    return out


def deserialize_json(data: dict) -> PieChartFieldWells:
    out: PieChartFieldWells = {}  # type: ignore[typeddict-item]
    if "PieChartAggregatedFieldWells" in data:
        import aws_sdk_quicksight.types.pie_chart_aggregated_field_wells

        out["pie_chart_aggregated_field_wells"] = (
            aws_sdk_quicksight.types.pie_chart_aggregated_field_wells.deserialize_json(
                data["PieChartAggregatedFieldWells"]
            )
        )
    return out
