"""Generated from Smithy shape ``com.amazonaws.quicksight#LineChartFieldWells``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.line_chart_aggregated_field_wells


class LineChartFieldWells(TypedDict):
    line_chart_aggregated_field_wells: NotRequired[
        "aws_sdk_quicksight.types.line_chart_aggregated_field_wells.LineChartAggregatedFieldWells"
    ]
    """<p>The field well configuration of a line chart.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LineChartFieldWells) -> dict:
    out: dict = {}
    if "line_chart_aggregated_field_wells" in value:
        import aws_sdk_quicksight.types.line_chart_aggregated_field_wells

        out["LineChartAggregatedFieldWells"] = (
            aws_sdk_quicksight.types.line_chart_aggregated_field_wells.serialize_json(
                value["line_chart_aggregated_field_wells"]
            )
        )
    return out


def deserialize_json(data: dict) -> LineChartFieldWells:
    out: LineChartFieldWells = {}  # type: ignore[typeddict-item]
    if "LineChartAggregatedFieldWells" in data:
        import aws_sdk_quicksight.types.line_chart_aggregated_field_wells

        out["line_chart_aggregated_field_wells"] = (
            aws_sdk_quicksight.types.line_chart_aggregated_field_wells.deserialize_json(
                data["LineChartAggregatedFieldWells"]
            )
        )
    return out
