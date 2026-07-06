"""Generated from Smithy shape ``com.amazonaws.quicksight#ComboChartFieldWells``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.combo_chart_aggregated_field_wells


class ComboChartFieldWells(TypedDict, closed=True):
    combo_chart_aggregated_field_wells: NotRequired[
        "aws_sdk_quicksight.types.combo_chart_aggregated_field_wells.ComboChartAggregatedFieldWells"
    ]
    """<p>The aggregated field wells of a combo chart. Combo charts only have aggregated field wells. Columns in a combo chart are aggregated by category.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ComboChartFieldWells) -> dict:
    out: dict = {}
    if "combo_chart_aggregated_field_wells" in value:
        import aws_sdk_quicksight.types.combo_chart_aggregated_field_wells

        out["ComboChartAggregatedFieldWells"] = (
            aws_sdk_quicksight.types.combo_chart_aggregated_field_wells.serialize_json(
                value["combo_chart_aggregated_field_wells"]
            )
        )
    return out


def deserialize_json(data: dict) -> ComboChartFieldWells:
    out: ComboChartFieldWells = {}  # type: ignore[typeddict-item]
    if "ComboChartAggregatedFieldWells" in data:
        import aws_sdk_quicksight.types.combo_chart_aggregated_field_wells

        out["combo_chart_aggregated_field_wells"] = (
            aws_sdk_quicksight.types.combo_chart_aggregated_field_wells.deserialize_json(
                data["ComboChartAggregatedFieldWells"]
            )
        )
    return out
