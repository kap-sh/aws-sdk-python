"""Generated from Smithy shape ``com.amazonaws.quicksight#FunnelChartFieldWells``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.funnel_chart_aggregated_field_wells


class FunnelChartFieldWells(TypedDict):
    funnel_chart_aggregated_field_wells: NotRequired[
        "aws_sdk_quicksight.types.funnel_chart_aggregated_field_wells.FunnelChartAggregatedFieldWells"
    ]
    """<p>The field well configuration of a <code>FunnelChartVisual</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FunnelChartFieldWells) -> dict:
    out: dict = {}
    if "funnel_chart_aggregated_field_wells" in value:
        import aws_sdk_quicksight.types.funnel_chart_aggregated_field_wells

        out["FunnelChartAggregatedFieldWells"] = (
            aws_sdk_quicksight.types.funnel_chart_aggregated_field_wells.serialize_json(
                value["funnel_chart_aggregated_field_wells"]
            )
        )
    return out


def deserialize_json(data: dict) -> FunnelChartFieldWells:
    out: FunnelChartFieldWells = {}  # type: ignore[typeddict-item]
    if "FunnelChartAggregatedFieldWells" in data:
        import aws_sdk_quicksight.types.funnel_chart_aggregated_field_wells

        out["funnel_chart_aggregated_field_wells"] = (
            aws_sdk_quicksight.types.funnel_chart_aggregated_field_wells.deserialize_json(
                data["FunnelChartAggregatedFieldWells"]
            )
        )
    return out
