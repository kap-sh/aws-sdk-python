"""Generated from Smithy shape ``com.amazonaws.quicksight#PivotFieldSortOptions``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.field_id
    import aws_sdk_quicksight.types.pivot_table_sort_by


class PivotFieldSortOptions(TypedDict):
    field_id: "aws_sdk_quicksight.types.field_id.FieldId"
    """<p>The field ID for the field sort options.</p>"""
    sort_by: "aws_sdk_quicksight.types.pivot_table_sort_by.PivotTableSortBy"
    """<p>The sort by field for the field sort options.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PivotFieldSortOptions) -> dict:
    out: dict = {}
    out["FieldId"] = value["field_id"]
    import aws_sdk_quicksight.types.pivot_table_sort_by

    out["SortBy"] = aws_sdk_quicksight.types.pivot_table_sort_by.serialize_json(
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
        import aws_sdk_quicksight.types.pivot_table_sort_by

        out["sort_by"] = aws_sdk_quicksight.types.pivot_table_sort_by.deserialize_json(
            data["SortBy"]
        )
    else:
        raise DeserializationError("PivotFieldSortOptions.sort_by required")
    return out
