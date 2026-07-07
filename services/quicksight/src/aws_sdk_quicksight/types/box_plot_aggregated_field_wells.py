"""Generated from Smithy shape ``com.amazonaws.quicksight#BoxPlotAggregatedFieldWells``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.box_plot_dimension_field_list
    import aws_sdk_quicksight.types.box_plot_measure_field_list


class BoxPlotAggregatedFieldWells(TypedDict, closed=True):
    group_by: NotRequired[
        "aws_sdk_quicksight.types.box_plot_dimension_field_list.BoxPlotDimensionFieldList"
    ]
    """<p>The group by field well of a box plot chart. Values are grouped based on group by fields.</p>"""
    values: NotRequired[
        "aws_sdk_quicksight.types.box_plot_measure_field_list.BoxPlotMeasureFieldList"
    ]
    """<p>The value field well of a box plot chart. Values are aggregated based on group by fields.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BoxPlotAggregatedFieldWells) -> dict:
    out: dict = {}
    if "group_by" in value:
        import aws_sdk_quicksight.types.box_plot_dimension_field_list

        out["GroupBy"] = (
            aws_sdk_quicksight.types.box_plot_dimension_field_list.serialize_json(
                value["group_by"]
            )
        )
    if "values" in value:
        import aws_sdk_quicksight.types.box_plot_measure_field_list

        out["Values"] = (
            aws_sdk_quicksight.types.box_plot_measure_field_list.serialize_json(
                value["values"]
            )
        )
    return out


def deserialize_json(data: dict) -> BoxPlotAggregatedFieldWells:
    out: BoxPlotAggregatedFieldWells = {}  # type: ignore[typeddict-item]
    if "GroupBy" in data:
        import aws_sdk_quicksight.types.box_plot_dimension_field_list

        out["group_by"] = (
            aws_sdk_quicksight.types.box_plot_dimension_field_list.deserialize_json(
                data["GroupBy"]
            )
        )
    if "Values" in data:
        import aws_sdk_quicksight.types.box_plot_measure_field_list

        out["values"] = (
            aws_sdk_quicksight.types.box_plot_measure_field_list.deserialize_json(
                data["Values"]
            )
        )
    return out
