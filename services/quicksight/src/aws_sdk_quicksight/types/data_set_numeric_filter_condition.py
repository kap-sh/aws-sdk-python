"""Generated from Smithy shape ``com.amazonaws.quicksight#DataSetNumericFilterCondition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.column_name
    import aws_sdk_quicksight.types.data_set_numeric_comparison_filter_condition
    import aws_sdk_quicksight.types.data_set_numeric_range_filter_condition


class DataSetNumericFilterCondition(TypedDict, closed=True):
    column_name: NotRequired["aws_sdk_quicksight.types.column_name.ColumnName"]
    """<p>The name of the numeric column to filter.</p>"""
    comparison_filter_condition: NotRequired[
        "aws_sdk_quicksight.types.data_set_numeric_comparison_filter_condition.DataSetNumericComparisonFilterCondition"
    ]
    """<p>A comparison-based filter condition for the numeric column.</p>"""
    range_filter_condition: NotRequired[
        "aws_sdk_quicksight.types.data_set_numeric_range_filter_condition.DataSetNumericRangeFilterCondition"
    ]
    """<p>A range-based filter condition for the numeric column, filtering values between minimum and maximum numbers.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataSetNumericFilterCondition) -> dict:
    out: dict = {}
    if "column_name" in value:
        out["ColumnName"] = value["column_name"]
    if "comparison_filter_condition" in value:
        import aws_sdk_quicksight.types.data_set_numeric_comparison_filter_condition

        out["ComparisonFilterCondition"] = (
            aws_sdk_quicksight.types.data_set_numeric_comparison_filter_condition.serialize_json(
                value["comparison_filter_condition"]
            )
        )
    if "range_filter_condition" in value:
        import aws_sdk_quicksight.types.data_set_numeric_range_filter_condition

        out["RangeFilterCondition"] = (
            aws_sdk_quicksight.types.data_set_numeric_range_filter_condition.serialize_json(
                value["range_filter_condition"]
            )
        )
    return out


def deserialize_json(data: dict) -> DataSetNumericFilterCondition:
    out: DataSetNumericFilterCondition = {}  # type: ignore[typeddict-item]
    if "ColumnName" in data:
        out["column_name"] = data["ColumnName"]
    if "ComparisonFilterCondition" in data:
        import aws_sdk_quicksight.types.data_set_numeric_comparison_filter_condition

        out["comparison_filter_condition"] = (
            aws_sdk_quicksight.types.data_set_numeric_comparison_filter_condition.deserialize_json(
                data["ComparisonFilterCondition"]
            )
        )
    if "RangeFilterCondition" in data:
        import aws_sdk_quicksight.types.data_set_numeric_range_filter_condition

        out["range_filter_condition"] = (
            aws_sdk_quicksight.types.data_set_numeric_range_filter_condition.deserialize_json(
                data["RangeFilterCondition"]
            )
        )
    return out
