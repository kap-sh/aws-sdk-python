"""Generated from Smithy shape ``com.amazonaws.quicksight#FieldSortOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.column_sort
    import capo_quicksight.types.field_sort


class FieldSortOptions(TypedDict, closed=True):
    field_sort: NotRequired["capo_quicksight.types.field_sort.FieldSort"]
    """<p>The sort configuration for a field in a field well.</p>"""
    column_sort: NotRequired["capo_quicksight.types.column_sort.ColumnSort"]
    """<p>The sort configuration for a column that is not used in a field well.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FieldSortOptions) -> dict:
    out: dict = {}
    if "field_sort" in value:
        import capo_quicksight.types.field_sort

        out["FieldSort"] = capo_quicksight.types.field_sort.serialize_json(
            value["field_sort"]
        )
    if "column_sort" in value:
        import capo_quicksight.types.column_sort

        out["ColumnSort"] = capo_quicksight.types.column_sort.serialize_json(
            value["column_sort"]
        )
    return out


def deserialize_json(data: dict) -> FieldSortOptions:
    out: FieldSortOptions = {}  # type: ignore[typeddict-item]
    if "FieldSort" in data:
        import capo_quicksight.types.field_sort

        out["field_sort"] = capo_quicksight.types.field_sort.deserialize_json(
            data["FieldSort"]
        )
    if "ColumnSort" in data:
        import capo_quicksight.types.column_sort

        out["column_sort"] = capo_quicksight.types.column_sort.deserialize_json(
            data["ColumnSort"]
        )
    return out
