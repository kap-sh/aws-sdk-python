"""Generated from Smithy shape ``com.amazonaws.quicksight#PivotTableAggregatedFieldWells``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.pivot_measure_field_list
    import aws_sdk_quicksight.types.pivot_table_dimension_list


class PivotTableAggregatedFieldWells(TypedDict):
    rows: NotRequired[
        "aws_sdk_quicksight.types.pivot_table_dimension_list.PivotTableDimensionList"
    ]
    """<p>The rows field well for a pivot table. Values are grouped by rows fields.</p>"""
    columns: NotRequired[
        "aws_sdk_quicksight.types.pivot_table_dimension_list.PivotTableDimensionList"
    ]
    """<p>The columns field well for a pivot table. Values are grouped by columns fields.</p>"""
    values: NotRequired[
        "aws_sdk_quicksight.types.pivot_measure_field_list.PivotMeasureFieldList"
    ]
    """<p>The values field well for a pivot table. Values are aggregated based on rows and columns fields.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PivotTableAggregatedFieldWells) -> dict:
    out: dict = {}
    if "rows" in value:
        import aws_sdk_quicksight.types.pivot_table_dimension_list

        out["Rows"] = (
            aws_sdk_quicksight.types.pivot_table_dimension_list.serialize_json(
                value["rows"]
            )
        )
    if "columns" in value:
        import aws_sdk_quicksight.types.pivot_table_dimension_list

        out["Columns"] = (
            aws_sdk_quicksight.types.pivot_table_dimension_list.serialize_json(
                value["columns"]
            )
        )
    if "values" in value:
        import aws_sdk_quicksight.types.pivot_measure_field_list

        out["Values"] = (
            aws_sdk_quicksight.types.pivot_measure_field_list.serialize_json(
                value["values"]
            )
        )
    return out


def deserialize_json(data: dict) -> PivotTableAggregatedFieldWells:
    out: PivotTableAggregatedFieldWells = {}  # type: ignore[typeddict-item]
    if "Rows" in data:
        import aws_sdk_quicksight.types.pivot_table_dimension_list

        out["rows"] = (
            aws_sdk_quicksight.types.pivot_table_dimension_list.deserialize_json(
                data["Rows"]
            )
        )
    if "Columns" in data:
        import aws_sdk_quicksight.types.pivot_table_dimension_list

        out["columns"] = (
            aws_sdk_quicksight.types.pivot_table_dimension_list.deserialize_json(
                data["Columns"]
            )
        )
    if "Values" in data:
        import aws_sdk_quicksight.types.pivot_measure_field_list

        out["values"] = (
            aws_sdk_quicksight.types.pivot_measure_field_list.deserialize_json(
                data["Values"]
            )
        )
    return out
