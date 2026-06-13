"""Generated from Smithy shape ``com.amazonaws.quicksight#FunnelChartAggregatedFieldWells``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.funnel_chart_dimension_field_list
    import aws_sdk_quicksight.types.funnel_chart_measure_field_list


class FunnelChartAggregatedFieldWells(TypedDict):
    category: NotRequired[
        "aws_sdk_quicksight.types.funnel_chart_dimension_field_list.FunnelChartDimensionFieldList"
    ]
    """<p>The category field wells of a funnel chart. Values are grouped by category fields.</p>"""
    values: NotRequired[
        "aws_sdk_quicksight.types.funnel_chart_measure_field_list.FunnelChartMeasureFieldList"
    ]
    """<p>The value field wells of a funnel chart. Values are aggregated based on categories.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FunnelChartAggregatedFieldWells) -> dict:
    out: dict = {}
    if "category" in value:
        import aws_sdk_quicksight.types.funnel_chart_dimension_field_list

        out["Category"] = (
            aws_sdk_quicksight.types.funnel_chart_dimension_field_list.serialize_json(
                value["category"]
            )
        )
    if "values" in value:
        import aws_sdk_quicksight.types.funnel_chart_measure_field_list

        out["Values"] = (
            aws_sdk_quicksight.types.funnel_chart_measure_field_list.serialize_json(
                value["values"]
            )
        )
    return out


def deserialize_json(data: dict) -> FunnelChartAggregatedFieldWells:
    out: FunnelChartAggregatedFieldWells = {}  # type: ignore[typeddict-item]
    if "Category" in data:
        import aws_sdk_quicksight.types.funnel_chart_dimension_field_list

        out["category"] = (
            aws_sdk_quicksight.types.funnel_chart_dimension_field_list.deserialize_json(
                data["Category"]
            )
        )
    if "Values" in data:
        import aws_sdk_quicksight.types.funnel_chart_measure_field_list

        out["values"] = (
            aws_sdk_quicksight.types.funnel_chart_measure_field_list.deserialize_json(
                data["Values"]
            )
        )
    return out
