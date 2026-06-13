"""Generated from Smithy shape ``com.amazonaws.quicksight#DataSetDateFilterCondition``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.column_name
    import aws_sdk_quicksight.types.data_set_date_comparison_filter_condition
    import aws_sdk_quicksight.types.data_set_date_range_filter_condition


class DataSetDateFilterCondition(TypedDict):
    column_name: NotRequired["aws_sdk_quicksight.types.column_name.ColumnName"]
    """<p>The name of the date column to filter.</p>"""
    comparison_filter_condition: NotRequired[
        "aws_sdk_quicksight.types.data_set_date_comparison_filter_condition.DataSetDateComparisonFilterCondition"
    ]
    """<p>A comparison-based filter condition for the date column.</p>"""
    range_filter_condition: NotRequired[
        "aws_sdk_quicksight.types.data_set_date_range_filter_condition.DataSetDateRangeFilterCondition"
    ]
    """<p>A range-based filter condition for the date column, filtering values between minimum and maximum dates.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataSetDateFilterCondition) -> dict:
    out: dict = {}
    if "column_name" in value:
        out["ColumnName"] = value["column_name"]
    if "comparison_filter_condition" in value:
        import aws_sdk_quicksight.types.data_set_date_comparison_filter_condition

        out["ComparisonFilterCondition"] = (
            aws_sdk_quicksight.types.data_set_date_comparison_filter_condition.serialize_json(
                value["comparison_filter_condition"]
            )
        )
    if "range_filter_condition" in value:
        import aws_sdk_quicksight.types.data_set_date_range_filter_condition

        out["RangeFilterCondition"] = (
            aws_sdk_quicksight.types.data_set_date_range_filter_condition.serialize_json(
                value["range_filter_condition"]
            )
        )
    return out


def deserialize_json(data: dict) -> DataSetDateFilterCondition:
    out: DataSetDateFilterCondition = {}  # type: ignore[typeddict-item]
    if "ColumnName" in data:
        out["column_name"] = data["ColumnName"]
    if "ComparisonFilterCondition" in data:
        import aws_sdk_quicksight.types.data_set_date_comparison_filter_condition

        out["comparison_filter_condition"] = (
            aws_sdk_quicksight.types.data_set_date_comparison_filter_condition.deserialize_json(
                data["ComparisonFilterCondition"]
            )
        )
    if "RangeFilterCondition" in data:
        import aws_sdk_quicksight.types.data_set_date_range_filter_condition

        out["range_filter_condition"] = (
            aws_sdk_quicksight.types.data_set_date_range_filter_condition.deserialize_json(
                data["RangeFilterCondition"]
            )
        )
    return out
