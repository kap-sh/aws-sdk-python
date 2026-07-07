"""Generated from Smithy shape ``com.amazonaws.quicksight#PivotTableSortBy``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.column_sort
    import aws_sdk_quicksight.types.data_path_sort
    import aws_sdk_quicksight.types.field_sort


class PivotTableSortBy(TypedDict, closed=True):
    field: NotRequired["aws_sdk_quicksight.types.field_sort.FieldSort"]
    """<p>The field sort (field id, direction) for the pivot table sort by options.</p>"""
    column: NotRequired["aws_sdk_quicksight.types.column_sort.ColumnSort"]
    """<p>The column sort (field id, direction) for the pivot table sort by options.</p>"""
    data_path: NotRequired["aws_sdk_quicksight.types.data_path_sort.DataPathSort"]
    """<p>The data path sort (data path value, direction) for the pivot table sort by options.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PivotTableSortBy) -> dict:
    out: dict = {}
    if "field" in value:
        import aws_sdk_quicksight.types.field_sort

        out["Field"] = aws_sdk_quicksight.types.field_sort.serialize_json(
            value["field"]
        )
    if "column" in value:
        import aws_sdk_quicksight.types.column_sort

        out["Column"] = aws_sdk_quicksight.types.column_sort.serialize_json(
            value["column"]
        )
    if "data_path" in value:
        import aws_sdk_quicksight.types.data_path_sort

        out["DataPath"] = aws_sdk_quicksight.types.data_path_sort.serialize_json(
            value["data_path"]
        )
    return out


def deserialize_json(data: dict) -> PivotTableSortBy:
    out: PivotTableSortBy = {}  # type: ignore[typeddict-item]
    if "Field" in data:
        import aws_sdk_quicksight.types.field_sort

        out["field"] = aws_sdk_quicksight.types.field_sort.deserialize_json(
            data["Field"]
        )
    if "Column" in data:
        import aws_sdk_quicksight.types.column_sort

        out["column"] = aws_sdk_quicksight.types.column_sort.deserialize_json(
            data["Column"]
        )
    if "DataPath" in data:
        import aws_sdk_quicksight.types.data_path_sort

        out["data_path"] = aws_sdk_quicksight.types.data_path_sort.deserialize_json(
            data["DataPath"]
        )
    return out
