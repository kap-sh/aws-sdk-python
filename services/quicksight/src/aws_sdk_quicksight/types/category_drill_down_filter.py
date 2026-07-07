"""Generated from Smithy shape ``com.amazonaws.quicksight#CategoryDrillDownFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.category_value_list
    import aws_sdk_quicksight.types.column_identifier


class CategoryDrillDownFilter(TypedDict, closed=True):
    column: "aws_sdk_quicksight.types.column_identifier.ColumnIdentifier"
    """<p>The column that the filter is applied to.</p>"""
    category_values: "aws_sdk_quicksight.types.category_value_list.CategoryValueList"
    """<p>A list of the string inputs that are the values of the category drill down filter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CategoryDrillDownFilter) -> dict:
    out: dict = {}
    import aws_sdk_quicksight.types.column_identifier

    out["Column"] = aws_sdk_quicksight.types.column_identifier.serialize_json(
        value["column"]
    )
    import aws_sdk_quicksight.types.category_value_list

    out["CategoryValues"] = aws_sdk_quicksight.types.category_value_list.serialize_json(
        value["category_values"]
    )
    return out


def deserialize_json(data: dict) -> CategoryDrillDownFilter:
    out: CategoryDrillDownFilter = {}  # type: ignore[typeddict-item]
    if "Column" in data:
        import aws_sdk_quicksight.types.column_identifier

        out["column"] = aws_sdk_quicksight.types.column_identifier.deserialize_json(
            data["Column"]
        )
    else:
        raise DeserializationError("CategoryDrillDownFilter.column required")
    if "CategoryValues" in data:
        import aws_sdk_quicksight.types.category_value_list

        out["category_values"] = (
            aws_sdk_quicksight.types.category_value_list.deserialize_json(
                data["CategoryValues"]
            )
        )
    else:
        raise DeserializationError("CategoryDrillDownFilter.category_values required")
    return out
