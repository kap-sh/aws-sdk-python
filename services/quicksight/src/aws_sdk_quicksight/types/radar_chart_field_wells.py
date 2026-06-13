"""Generated from Smithy shape ``com.amazonaws.quicksight#RadarChartFieldWells``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.radar_chart_aggregated_field_wells


class RadarChartFieldWells(TypedDict):
    radar_chart_aggregated_field_wells: NotRequired[
        "aws_sdk_quicksight.types.radar_chart_aggregated_field_wells.RadarChartAggregatedFieldWells"
    ]
    """<p>The aggregated field wells of a radar chart visual.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RadarChartFieldWells) -> dict:
    out: dict = {}
    if "radar_chart_aggregated_field_wells" in value:
        import aws_sdk_quicksight.types.radar_chart_aggregated_field_wells

        out["RadarChartAggregatedFieldWells"] = (
            aws_sdk_quicksight.types.radar_chart_aggregated_field_wells.serialize_json(
                value["radar_chart_aggregated_field_wells"]
            )
        )
    return out


def deserialize_json(data: dict) -> RadarChartFieldWells:
    out: RadarChartFieldWells = {}  # type: ignore[typeddict-item]
    if "RadarChartAggregatedFieldWells" in data:
        import aws_sdk_quicksight.types.radar_chart_aggregated_field_wells

        out["radar_chart_aggregated_field_wells"] = (
            aws_sdk_quicksight.types.radar_chart_aggregated_field_wells.deserialize_json(
                data["RadarChartAggregatedFieldWells"]
            )
        )
    return out
