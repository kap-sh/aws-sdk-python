"""Generated from Smithy shape ``com.amazonaws.quicksight#HeatMapAggregatedFieldWells``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.heat_map_dimension_field_list
    import aws_sdk_quicksight.types.heat_map_measure_field_list


class HeatMapAggregatedFieldWells(TypedDict, closed=True):
    rows: NotRequired[
        "aws_sdk_quicksight.types.heat_map_dimension_field_list.HeatMapDimensionFieldList"
    ]
    """<p>The rows field well of a heat map.</p>"""
    columns: NotRequired[
        "aws_sdk_quicksight.types.heat_map_dimension_field_list.HeatMapDimensionFieldList"
    ]
    """<p>The columns field well of a heat map.</p>"""
    values: NotRequired[
        "aws_sdk_quicksight.types.heat_map_measure_field_list.HeatMapMeasureFieldList"
    ]
    """<p>The values field well of a heat map.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HeatMapAggregatedFieldWells) -> dict:
    out: dict = {}
    if "rows" in value:
        import aws_sdk_quicksight.types.heat_map_dimension_field_list

        out["Rows"] = (
            aws_sdk_quicksight.types.heat_map_dimension_field_list.serialize_json(
                value["rows"]
            )
        )
    if "columns" in value:
        import aws_sdk_quicksight.types.heat_map_dimension_field_list

        out["Columns"] = (
            aws_sdk_quicksight.types.heat_map_dimension_field_list.serialize_json(
                value["columns"]
            )
        )
    if "values" in value:
        import aws_sdk_quicksight.types.heat_map_measure_field_list

        out["Values"] = (
            aws_sdk_quicksight.types.heat_map_measure_field_list.serialize_json(
                value["values"]
            )
        )
    return out


def deserialize_json(data: dict) -> HeatMapAggregatedFieldWells:
    out: HeatMapAggregatedFieldWells = {}  # type: ignore[typeddict-item]
    if "Rows" in data:
        import aws_sdk_quicksight.types.heat_map_dimension_field_list

        out["rows"] = (
            aws_sdk_quicksight.types.heat_map_dimension_field_list.deserialize_json(
                data["Rows"]
            )
        )
    if "Columns" in data:
        import aws_sdk_quicksight.types.heat_map_dimension_field_list

        out["columns"] = (
            aws_sdk_quicksight.types.heat_map_dimension_field_list.deserialize_json(
                data["Columns"]
            )
        )
    if "Values" in data:
        import aws_sdk_quicksight.types.heat_map_measure_field_list

        out["values"] = (
            aws_sdk_quicksight.types.heat_map_measure_field_list.deserialize_json(
                data["Values"]
            )
        )
    return out
