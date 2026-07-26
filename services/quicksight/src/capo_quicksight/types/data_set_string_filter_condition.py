"""Generated from Smithy shape ``com.amazonaws.quicksight#DataSetStringFilterCondition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.column_name
    import capo_quicksight.types.data_set_string_comparison_filter_condition
    import capo_quicksight.types.data_set_string_list_filter_condition


class DataSetStringFilterCondition(TypedDict, closed=True):
    column_name: NotRequired["capo_quicksight.types.column_name.ColumnName"]
    """<p>The name of the string column to filter.</p>"""
    comparison_filter_condition: NotRequired[
        "capo_quicksight.types.data_set_string_comparison_filter_condition.DataSetStringComparisonFilterCondition"
    ]
    """<p>A comparison-based filter condition for the string column.</p>"""
    list_filter_condition: NotRequired[
        "capo_quicksight.types.data_set_string_list_filter_condition.DataSetStringListFilterCondition"
    ]
    """<p>A list-based filter condition that includes or excludes values from a specified list.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataSetStringFilterCondition) -> dict:
    out: dict = {}
    if "column_name" in value:
        out["ColumnName"] = value["column_name"]
    if "comparison_filter_condition" in value:
        import capo_quicksight.types.data_set_string_comparison_filter_condition

        out["ComparisonFilterCondition"] = (
            capo_quicksight.types.data_set_string_comparison_filter_condition.serialize_json(
                value["comparison_filter_condition"]
            )
        )
    if "list_filter_condition" in value:
        import capo_quicksight.types.data_set_string_list_filter_condition

        out["ListFilterCondition"] = (
            capo_quicksight.types.data_set_string_list_filter_condition.serialize_json(
                value["list_filter_condition"]
            )
        )
    return out


def deserialize_json(data: dict) -> DataSetStringFilterCondition:
    out: DataSetStringFilterCondition = {}  # type: ignore[typeddict-item]
    if "ColumnName" in data:
        out["column_name"] = data["ColumnName"]
    if "ComparisonFilterCondition" in data:
        import capo_quicksight.types.data_set_string_comparison_filter_condition

        out["comparison_filter_condition"] = (
            capo_quicksight.types.data_set_string_comparison_filter_condition.deserialize_json(
                data["ComparisonFilterCondition"]
            )
        )
    if "ListFilterCondition" in data:
        import capo_quicksight.types.data_set_string_list_filter_condition

        out["list_filter_condition"] = (
            capo_quicksight.types.data_set_string_list_filter_condition.deserialize_json(
                data["ListFilterCondition"]
            )
        )
    return out
