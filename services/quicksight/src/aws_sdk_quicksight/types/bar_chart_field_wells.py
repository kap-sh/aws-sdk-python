"""Generated from Smithy shape ``com.amazonaws.quicksight#BarChartFieldWells``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.bar_chart_aggregated_field_wells


class BarChartFieldWells(TypedDict):
    bar_chart_aggregated_field_wells: NotRequired[
        "aws_sdk_quicksight.types.bar_chart_aggregated_field_wells.BarChartAggregatedFieldWells"
    ]
    """<p>The aggregated field wells of a bar chart.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BarChartFieldWells) -> dict:
    out: dict = {}
    if "bar_chart_aggregated_field_wells" in value:
        import aws_sdk_quicksight.types.bar_chart_aggregated_field_wells

        out["BarChartAggregatedFieldWells"] = (
            aws_sdk_quicksight.types.bar_chart_aggregated_field_wells.serialize_json(
                value["bar_chart_aggregated_field_wells"]
            )
        )
    return out


def deserialize_json(data: dict) -> BarChartFieldWells:
    out: BarChartFieldWells = {}  # type: ignore[typeddict-item]
    if "BarChartAggregatedFieldWells" in data:
        import aws_sdk_quicksight.types.bar_chart_aggregated_field_wells

        out["bar_chart_aggregated_field_wells"] = (
            aws_sdk_quicksight.types.bar_chart_aggregated_field_wells.deserialize_json(
                data["BarChartAggregatedFieldWells"]
            )
        )
    return out
