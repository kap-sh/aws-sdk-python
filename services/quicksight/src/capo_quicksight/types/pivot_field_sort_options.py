"""Generated from Smithy shape ``com.amazonaws.quicksight#PivotFieldSortOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.field_id
    import capo_quicksight.types.pivot_table_sort_by


class PivotFieldSortOptions(TypedDict, closed=True):
    field_id: "capo_quicksight.types.field_id.FieldId"
    """<p>The field ID for the field sort options.</p>"""
    sort_by: "capo_quicksight.types.pivot_table_sort_by.PivotTableSortBy"
    """<p>The sort by field for the field sort options.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PivotFieldSortOptions) -> dict:
    out: dict = {}
    out["FieldId"] = value["field_id"]
    import capo_quicksight.types.pivot_table_sort_by

    out["SortBy"] = capo_quicksight.types.pivot_table_sort_by.serialize_json(
        value["sort_by"]
    )
    return out


def deserialize_json(data: dict) -> PivotFieldSortOptions:
    out: PivotFieldSortOptions = {}  # type: ignore[typeddict-item]
    if "FieldId" in data:
        out["field_id"] = data["FieldId"]
    else:
        raise DeserializationError("PivotFieldSortOptions.field_id required")
    if "SortBy" in data:
        import capo_quicksight.types.pivot_table_sort_by

        out["sort_by"] = capo_quicksight.types.pivot_table_sort_by.deserialize_json(
            data["SortBy"]
        )
    else:
        raise DeserializationError("PivotFieldSortOptions.sort_by required")
    return out
