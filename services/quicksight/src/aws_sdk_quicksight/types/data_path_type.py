"""Generated from Smithy shape ``com.amazonaws.quicksight#DataPathType``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.pivot_table_data_path_type


class DataPathType(TypedDict):
    pivot_table_data_path_type: NotRequired[
        "aws_sdk_quicksight.types.pivot_table_data_path_type.PivotTableDataPathType"
    ]
    """<p>The type of data path value utilized in a pivot table. Choose one of the following options:</p> <ul> <li> <p> <code>HIERARCHY_ROWS_LAYOUT_COLUMN</code> - The type of data path for the rows layout column, when <code>RowsLayout</code> is set to <code>HIERARCHY</code>.</p> </li> <li> <p> <code>MULTIPLE_ROW_METRICS_COLUMN</code> - The type of data path for the metric column when the row is set to Metric Placement.</p> </li> <li> <p> <code>EMPTY_COLUMN_HEADER</code> - The type of data path for the column with empty column header, when there is no field in <code>ColumnsFieldWell</code> and the row is set to Metric Placement.</p> </li> <li> <p> <code>COUNT_METRIC_COLUMN</code> - The type of data path for the column with <code>COUNT</code> as the metric, when there is no field in the <code>ValuesFieldWell</code>.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataPathType) -> dict:
    out: dict = {}
    if "pivot_table_data_path_type" in value:
        import aws_sdk_quicksight.types.pivot_table_data_path_type

        out["PivotTableDataPathType"] = (
            aws_sdk_quicksight.types.pivot_table_data_path_type.serialize_json(
                value["pivot_table_data_path_type"]
            )
        )
    return out


def deserialize_json(data: dict) -> DataPathType:
    out: DataPathType = {}  # type: ignore[typeddict-item]
    if "PivotTableDataPathType" in data:
        import aws_sdk_quicksight.types.pivot_table_data_path_type

        out["pivot_table_data_path_type"] = (
            aws_sdk_quicksight.types.pivot_table_data_path_type.deserialize_json(
                data["PivotTableDataPathType"]
            )
        )
    return out
